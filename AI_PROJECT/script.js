let books = JSON.parse(localStorage.getItem('libraryBooks')) || [];
let issues = JSON.parse(localStorage.getItem('libraryIssues')) || [];
let returns = JSON.parse(localStorage.getItem('libraryReturns')) || [];

let selectedBookIndex = -1;

/* ==================== ELEMENTS ==================== */
const bookBody = document.getElementById('bookBody');
const issuedCountEl = document.getElementById('issuedCount');
const overdueCountEl = document.getElementById('overdueCount');
const totalBooksEl = document.getElementById('totalBooks');
const toast = document.getElementById('toast');
const issueBtnText = document.getElementById('issueBtnText');
const issueSpinner = document.getElementById('issueSpinner');

/* ==================== INIT ==================== */
document.addEventListener('DOMContentLoaded', () => {
  renderTable();
  updateDashboard();
  setupSearch();
  setupModals();
  loadTheme();
});

/* ==================== THEME ==================== */
function loadTheme() {
  const theme = localStorage.getItem('theme') || 'light';
  document.documentElement.setAttribute('data-theme', theme);
  document.querySelector('.theme-toggle i')
    .classList.add(theme === 'dark' ? 'fa-sun' : 'fa-moon');
}
function toggleTheme() {
  const cur = document.documentElement.getAttribute('data-theme');
  const next = cur === 'dark' ? 'light' : 'dark';
  document.documentElement.setAttribute('data-theme', next);
  localStorage.setItem('theme', next);
  document.querySelector('.theme-toggle i').classList.toggle('fa-sun');
  document.querySelector('.theme-toggle i').classList.toggle('fa-moon');
}

/* ==================== STORAGE ==================== */
function saveData() {
  localStorage.setItem('libraryBooks', JSON.stringify(books));
  localStorage.setItem('libraryIssues', JSON.stringify(issues));
  localStorage.setItem('libraryReturns', JSON.stringify(returns));
}

/* ==================== UI HELPERS ==================== */
function showToast(msg, type = 'success') {
  toast.innerHTML = `<i class="fas fa-${type === 'error' ? 'times' : 'check'}-circle"></i> ${msg}`;
  toast.className = 'toast' + (type === 'error' ? ' error' : '');
  toast.classList.add('show');
  setTimeout(() => toast.classList.remove('show'), 3000);
}

function launchConfetti() {
  const canvas = document.getElementById('confetti');
  const ctx = canvas.getContext('2d');
  canvas.width = window.innerWidth;
  canvas.height = window.innerHeight;
  canvas.style.display = 'block';
  const confetti = [];
  for (let i = 0; i < 300; i++) {
    confetti.push({
      x: Math.random() * canvas.width,
      y: Math.random() * canvas.height - canvas.height,
      r: Math.random() * 4 + 1,
      d: Math.random() * 300,
      color: `hsl(${Math.random() * 360},100%,50%)`,
      tilt: Math.random() * 10 - 10,
      tiltAngle: 0
    });
  }
  function draw() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    confetti.forEach((c, i) => {
      c.tiltAngle += 0.1;
      c.tilt = Math.sin(c.tiltAngle) * 15;
      ctx.beginPath();
      ctx.lineWidth = c.r;
      ctx.strokeStyle = c.color;
      ctx.moveTo(c.x + c.tilt + c.r / 2, c.y);
      ctx.lineTo(c.x + c.tilt, c.y + c.tilt + c.r / 2);
      ctx.stroke();
      c.y += c.d / 100;
      if (c.y > canvas.height) confetti[i] = { ...c, y: -20 };
    });
    requestAnimationFrame(draw);
  }
  draw();
  setTimeout(() => canvas.style.display = 'none', 5000);
}

/* ==================== DASHBOARD ==================== */
function updateDashboard() {
  const issued = issues.filter(i => !i.returned).length;
  const overdue = issues.filter(i => !i.returned && new Date(i.returnDate) < new Date()).length;
  issuedCountEl.textContent = issued;
  overdueCountEl.textContent = overdue;
  totalBooksEl.textContent = books.reduce((sum, b) => sum + b.totalCopies, 0);
}

/* ==================== RETURN LOGIC ==================== */
window.doReturn = function(issueId) {
  const issue = issues.find(i => i.id === issueId);
  if (!issue) return showToast('Issue not found!', 'error');

  issue.returned = true;
  issue.actualReturnDate = new Date().toISOString().split('T')[0];
  returns.push({ ...issue, returnTime: new Date().toLocaleString() });
  saveData();
  renderTable();
  updateDashboard();
  showToast('Returned successfully!', 'success');
  launchConfetti();
  showReceipt(issue);
  closeReturnModal();
};

/* ==================== RECEIPT ==================== */
function showReceipt(issue) {
  const book = books[issue.bookId];
  document.getElementById('receiptBody').innerHTML = `
    <h3>Return Receipt</h3>
    <p><strong>Book:</strong> ${book.title} by ${book.author}</p>
    <p><strong>Student:</strong> ${issue.name} (${issue.studentId})</p>
    <p><strong>Issued:</strong> ${issue.issueDate}</p>
    <p><strong>Due:</strong> ${issue.returnDate}</p>
    <p><strong>Returned:</strong> ${issue.actualReturnDate}</p>
    <hr><small>Thank you! Keep reading!</small>
  `;
  document.getElementById('receiptModal').style.display = 'flex';
}
function printReceipt() { window.print(); }
function downloadReceipt() {
  const a = document.createElement('a');
  a.href = 'data:text/plain,' + encodeURIComponent(document.getElementById('receiptBody').innerText);
  a.download = 'return-receipt.txt';
  a.click();
}
function closeReceipt() { document.getElementById('receiptModal').style.display = 'none'; }

/* ==================== TABLE RENDERING ==================== */
function renderTable(filter = '') {
  bookBody.innerHTML = '';
  const lower = filter.toLowerCase();

  books.forEach((book, idx) => {
    const active = issues.filter(i => i.bookId === idx && !i.returned);
    const avail = book.totalCopies - active.length;

    if (filter) {
      const matchesBook = book.title.toLowerCase().includes(lower) || book.author.toLowerCase().includes(lower);
      const matchesStudent = active.some(i => i.name.toLowerCase().includes(lower) || i.studentId.toLowerCase().includes(lower));
      if (!matchesBook && !matchesStudent) return;
    }

    const row = document.createElement('tr');
    row.dataset.index = idx;
    row.onclick = () => selectRow(idx);
    if (selectedBookIndex === idx) row.classList.add('selected');

    row.innerHTML = `
      <td><strong>${book.title}</strong></td>
      <td>${book.author}</td>
      <td>${book.totalCopies}</td>
      <td>${active.length}</td>
      <td><strong style="color:#2ecc71;">${avail}</strong></td>
      <td>${active.map(i => `${i.name}<br><small>${i.studentId}</small>`).join('<br>') || '-'}</td>
      <td>${active.map(i => i.issueDate).join('<br>') || '-'}</td>
      <td>${active.map(i => {
        const overdue = new Date(i.returnDate) < new Date();
        return `<span ${overdue ? 'class="overdue"' : ''}>${i.returnDate}</span>`;
      }).join('<br>') || '-'}</td>
      <td>${active.length ? `<button onclick="event.stopPropagation(); quickReturn(${idx})" class="btn-return">Return</button>` : '—'}</td>
    `;
    bookBody.appendChild(row);
  });

  updateDashboard();
}

window.quickReturn = function(bookId) {
  const active = issues.filter(i => i.bookId === bookId && !i.returned);
  if (active.length === 1) doReturn(active[0].id);
  else { selectedBookIndex = bookId; returnBook(); }
};

/* ==================== ISSUE BOOK ==================== */
function issueBook() {
  if (selectedBookIndex === -1) return showToast('Select a book first!', 'error');
  const book = books[selectedBookIndex];
  const active = issues.filter(i => i.bookId === selectedBookIndex && !i.returned);
  if (book.totalCopies <= active.length) return showToast('No copies available!', 'error');

  document.getElementById('issueInfo').innerHTML = `
    <strong>${book.title}</strong> by ${book.author}<br>
    <strong>Available:</strong> ${book.totalCopies - active.length}
  `;
  issueBtnText.textContent = 'Issue Now';
  issueSpinner.style.display = 'none';
  document.getElementById('issueModal').style.display = 'flex';
}

document.getElementById('issueForm').onsubmit = e => {
  e.preventDefault();
  const name = document.getElementById('issueName').value.trim();
  const sid = document.getElementById('issueId').value.trim();
  if (!name || !sid) return showToast('Fill all fields!', 'error');

  issueBtnText.textContent = 'Issuing...';
  issueSpinner.style.display = 'inline-block';

  setTimeout(() => {
    issues.push({
      id: Date.now(),
      bookId: selectedBookIndex,
      name, studentId: sid,
      issueDate: new Date().toISOString().split('T')[0],
      returnDate: new Date(Date.now() + 14 * 86400000).toISOString().split('T')[0],
      returned: false
    });
    saveData();
    renderTable();
    updateDashboard();
    showToast(`Issued to ${name}!`, 'success');
    document.getElementById('issueForm').reset();
    closeIssueModal();
  }, 800);
};

/* ==================== RETURN BOOK ==================== */
function returnBook() {
  if (selectedBookIndex === -1) return showToast('Select a book!', 'error');
  const active = issues.filter(i => i.bookId === selectedBookIndex && !i.returned);
  if (!active.length) return showToast('Nothing issued!', 'error');

  let list = '';
  active.forEach(iss => {
    list += `<div onclick="doReturn(${iss.id})" class="return-card">
      <strong>${iss.name}</strong> (${iss.studentId})<br>
      <small>Issued: ${iss.issueDate} | Due: ${iss.returnDate}</small>
    </div>`;
  });
  document.getElementById('returnList').innerHTML = list;
  document.getElementById('returnModal').style.display = 'flex';
}

/* ==================== ADD BOOK ==================== */
document.getElementById('addBookForm').onsubmit = e => {
  e.preventDefault();
  const title = document.getElementById('bookTitle').value.trim();
  const author = document.getElementById('bookAuthor').value.trim();
  const copies = parseInt(document.getElementById('bookCopies').value);
  if (!title || !author || copies < 1) return showToast('Invalid data!', 'error');

  books.push({ title, author, totalCopies: copies });
  saveData();
  closeAddModal();
  renderTable();
  showToast(`"${title}" added!`);
};

/* ==================== MISC HELPERS ==================== */
function setupSearch() {
  document.getElementById('searchInput').addEventListener('input', () => {
    renderTable(document.getElementById('searchInput').value);
  });
}
function refreshTable() {
  document.getElementById('searchInput').value = '';
  renderTable();
  showToast('Refreshed!');
}
function selectRow(i) {
  selectedBookIndex = i;
  renderTable(document.getElementById('searchInput').value);
}
function setupModals() {
  window.onclick = e => {
    if (e.target.classList.contains('modal')) e.target.style.display = 'none';
  };
}

/* Close Functions */
function openAddModal() { document.getElementById('addModal').style.display = 'flex'; }
function closeAddModal() { document.getElementById('addModal').style.display = 'none'; }
function closeIssueModal() { 
  document.getElementById('issueModal').style.display = 'none';
  issueBtnText.textContent = 'Issue Now';
  issueSpinner.style.display = 'none';
}
function closeReturnModal() { document.getElementById('returnModal').style.display = 'none'; }
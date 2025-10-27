from flask import Flask, render_template_string, request

app = Flask(__name__)

form_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Conference Registration</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background: #f5f7fb; }
        .reg-container {
            max-width: 480px;
            margin: 40px auto;
            background: #fff;
            padding: 32px 28px;
            border-radius: 9px;
            box-shadow: 0 8px 32px rgba(0,0,0,0.11);
        }
        h2 { text-align: center; color: #233a53; margin-bottom: 24px; }
        label {
            display: block;
            margin-bottom: .5em;
            color: #2b405c;
            font-weight: 500;
        }
        input, select {
            width: 100%;
            padding: 8px 10px;
            margin-bottom: 16px;
            border: 1px solid #afc4d6;
            border-radius: 4px;
            font-size: 1em;
        }
        button {
            width: 100%;
            padding: 10px 0;
            background: #386998;
            color: #fff;
            font-size: 1.1em;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-weight: bold;
            transition: background 0.2s;
        }
        button:hover, button:focus {
            background: #294d70;
        }
        .error-msg {
            color: #a81227;
            margin: -12px 0 12px 0;
            font-size: .98em;
            display: block;
        }
        .success {
            padding: 18px;
            background: #e4f5ea;
            color: #185f28;
            border-radius: 4px;
            text-align: center;
            font-weight: bold;
        }
        @media (max-width: 550px) {
            .reg-container { padding: 18px 5vw; }
        }
    </style>
</head>
<body>
    <div class="reg-container" aria-labelledby="formTitle">
        {% if registered %}
            <div class="success" role="status" aria-live="polite">
                Thank you for registering, {{ name }}! 
            </div>
        {% else %}
            <h2 id="formTitle">Conference Registration</h2>
            <form id="regForm" method="POST" novalidate aria-label="Conference Registration Form">
                <label for="name">Full Name<span aria-hidden="true">*</span></label>
                <input type="text" id="name" name="name" autocomplete="name" aria-required="true" required />

                <label for="email">Email<span aria-hidden="true">*</span></label>
                <input type="email" id="email" name="email" autocomplete="email" aria-required="true" required />

                <label for="phone">Phone Number<span aria-hidden="true">*</span></label>
                <input type="tel" id="phone" name="phone" autocomplete="tel" aria-required="true" 
                    pattern="^\\+?[0-9\\-\\s\\(\\)]{7,}$" required 
                    aria-describedby="phoneHelp" />
                <span id="phoneHelp" style="font-size:0.93em;color:#555;">E.g., +1 555-123-4567</span>

                <label for="session">Session<span aria-hidden="true">*</span></label>
                <select id="session" name="session" aria-required="true" required>
                    <option value="" disabled selected>Choose a session</option>
                    <option>AI in Everyday Life</option>
                    <option>Cloud Computing Essentials</option>
                    <option>UX Design for All</option>
                    <option>Future of Web Development</option>
                </select>
                
                <span id="formError" class="error-msg" aria-live="assertive" style="display:none;"></span>
                <button type="submit">Register</button>
            </form>
        {% endif %}
    </div>
    <script>
        // Simple AI-inspired validation: check for all required fields, valid email, phone, and selection
        (function() {
            const form = document.getElementById('regForm');
            if (!form) return;
            form.addEventListener('submit', function(e) {
                let errMsg = "";
                const name = form.name.value.trim();
                const email = form.email.value.trim();
                const phone = form.phone.value.trim();
                const session = form.session.value;
                const phonePattern = /^\\+?[0-9\\-\\s\\(\\)]{7,}$/;
                // AI-guided validation with user-friendly errors
                if (!name) {
                    errMsg = "Please enter your full name.";
                } else if (!email) {
                    errMsg = "Email is required.";
                } else if (!/^\\S+@\\S+\\.\\S+$/.test(email)) {
                    errMsg = "Please enter a valid email address.";
                } else if (!phone) {
                    errMsg = "Phone number is required.";
                } else if (!phonePattern.test(phone)) {
                    errMsg = "Please enter a valid phone number.";
                } else if (!session) {
                    errMsg = "Please select a session.";
                }
                if (errMsg) {
                    e.preventDefault();
                    const errSpan = document.getElementById('formError');
                    errSpan.textContent = errMsg;
                    errSpan.style.display = "block";
                    form.querySelectorAll('input, select')[0].focus();
                }
            });

            // Accessibility: Show when user corrects errors
            form.querySelectorAll('input, select').forEach(elem => {
                elem.addEventListener('input', () => {
                    document.getElementById('formError').style.display = "none";
                });
            });
        })();
    </script>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        phone = request.form.get('phone', '').strip()
        session_selected = request.form.get('session', '')
        # Simple re-validation on server
        if not (name and email and phone and session_selected):
            return render_template_string(form_template, registered=False)
        return render_template_string(form_template, registered=True, name=name)
    return render_template_string(form_template, registered=False)

if __name__ == "__main__":
    app.run(debug=True)


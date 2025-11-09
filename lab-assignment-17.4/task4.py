import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Install required resources (only first run)
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')

# ------------------------------
# Step 1: Create a sample social media dataset
# ------------------------------
data = {
    'post_id': [1, 2, 3, 4, 5],
    'username': ['user1', 'user2', 'user3', 'user4', 'user5'],
    'post_text': [
        "I love this product! 😍 Check it out: https://example.com/product",
        "Terrible experience... won't buy again!!! 💔 #disappointed",
        "It's okay, not great but not bad either. :)",
        "Best purchase ever!!! 👍👍👍 http://shopnow.com",
        "Waste of money :( totally useless!"
    ]
}

df = pd.DataFrame(data)
print("Original Dataset:\n", df, "\n")

# ------------------------------
# Step 2: Clean text (remove URLs, emojis, special characters)
# ------------------------------
def clean_text(text):
    text = re.sub(r'http\S+|www\S+', '', text)  # Remove URLs
    text = re.sub(r'[^A-Za-z\s]', '', text)     # Remove special chars/emojis
    text = text.lower()                         # Convert to lowercase
    return text

df['clean_text'] = df['post_text'].apply(clean_text)

# ------------------------------
# Step 3: Tokenization & stopword removal
# ------------------------------
stop_words = set(stopwords.words('english'))
df['tokens'] = df['clean_text'].apply(lambda x: [word for word in x.split() if word not in stop_words])

# ------------------------------
# Step 4: Lemmatization
# ------------------------------
lemmatizer = WordNetLemmatizer()
df['lemmatized'] = df['tokens'].apply(lambda words: [lemmatizer.lemmatize(w) for w in words])

# ------------------------------
# Step 5: Combine lemmatized tokens
# ------------------------------
df['processed_text'] = df['lemmatized'].apply(lambda x: ' '.join(x))

# ------------------------------
# Step 6: Drop extra columns
# ------------------------------
df_final = df.drop(columns=['post_text', 'clean_text', 'tokens', 'lemmatized'])

# ------------------------------
# Step 7: Save to CSV
# ------------------------------
output_path = "cleaned_social_media_data.csv"
df_final.to_csv(output_path, index=False)
print(f"✅ Cleaned dataset saved as '{output_path}'")
print("\nProcessed Dataset:\n", df_final)

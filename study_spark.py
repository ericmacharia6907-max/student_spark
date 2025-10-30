import streamlit as st

# List of 50 motivational quotes with authors
quotes = [
    ("The future belongs to those who believe the beauty the dreams.", "Eleanor Roosevelt"),
    ("The expert in anything was once a beginner.", ""),
    ("Strive for progress, not perfection.", ""),
    ("The mind is not a vessel to be filled, but a fire to be kindled.", ""),
    ("Believe you can and you're halfway there.", "Theodore Roosevelt"),
    ("Success is not final, failure is not fatal: It is the courage to continue that counts.", "Winston Churchill"),
    ("Don't watch the clock; do what it does. Keep going.", "Sam Levenson"),
    ("You miss 100% of the shots you don’t take.", "Wayne Gretzky"),
    ("Whether you think you can or you think you can’t, you’re right.", "Henry Ford"),
    ("Act as if what you do makes a difference. It does.", "William James"),
    ("Success usually comes to those who are too busy to be looking for it.", "Henry David Thoreau"),
    ("The way to get started is to quit talking and begin doing.", "Walt Disney"),
    ("Motivation is what gets you started. Habit is what keeps you going.", "Jim Ryun"),
    ("Don't be pushed around by the fears in your mind. Be led by the dreams in your heart.", "Roy T. Bennett"),
    ("Perseverance is failing 19 times and succeeding the 20th.", "Julie Andrews"),
    ("Hardships often prepare ordinary people for an extraordinary destiny.", "C.S. Lewis"),
    ("Dream big and dare to fail.", "Norman Vaughan"),
    ("You don't have to be great to start, but you have to start to be great.", ""),
    ("It does not matter how slowly you go as long as you do not stop.", "Confucius"),
    ("Success is the sum of small efforts, repeated day in and day out.", "Robert Collier"),
    ("Keep your eyes on the stars, and your feet on the ground.", "Theodore Roosevelt"),
    ("The harder the battle, the sweeter the victory.", ""),
    ("Believe in yourself and all that you are.", "Christian D. Larson"),
    ("Don't limit your challenges. Challenge your limits.", ""),
    ("Start where you are. Use what you have. Do what you can.", "Arthur Ashe"),
    ("The only place where success comes before work is in the dictionary.", "Vidal Sassoon"),
    ("Opportunities don't happen, you create them.", "Chris Grosser"),
    ("Don't wait for opportunity. Create it.", ""),
    ("Failure will never overtake me if my determination to succeed is strong enough.", "Og Mandino"),
    ("Success is not how high you have climbed, but how you make a positive difference to the world.", "Roy T. Bennett"),
    ("Don't stop when you're tired. Stop when you're done.", ""),
    ("The secret of getting ahead is getting started.", "Mark Twain"),
    ("Your limitation—it’s only your imagination.", ""),
    ("Push yourself, because no one else is going to do it for you.", ""),
    ("Great things never come from comfort zones.", ""),
    ("Dream it. Wish it. Do it.", ""),
    ("Sometimes later becomes never. Do it now.", ""),
    ("Little things make big days.", ""),
    ("It’s going to be hard, but hard does not mean impossible.", ""),
    ("Don’t wait for the right moment. Create it.", ""),
    ("Great things take time.", ""),
    ("Don’t be afraid to give up the good to go for the great.", "John D. Rockefeller"),
    ("The only way to do great work is to love what you do.", "Steve Jobs"),
    ("Dream bigger. Do bigger.", ""),
    ("Don’t watch the clock; do what it does. Keep going.", "Sam Levenson"),
    ("Do something today that your future self will thank you for.", ""),
    ("Stay positive, work hard, make it happen.", "")
]

# Initialize session state
if 'quote_idx' not in st.session_state:
    st.session_state.quote_idx = 0
if 'favorites' not in st.session_state:
    st.session_state.favorites = []

# CSS for animations and styling
st.markdown("""
    <style>
    body {
        background-color: #14111e;
        color: #fff;
    }
    .quote-box {
        background: rgba(30,23,49,0.8);
        border: 2px solid #6655e0;
        box-shadow: 0 0 15px #6655e0;
        border-radius: 18px;
        padding: 32px 25px;
        margin-bottom: 24px;
        text-align: center;
        font-size: 21px;
    }
    button.css-1emrehy.edgvbvh3 {
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    button.css-1emrehy.edgvbvh3:hover {
        transform: scale(1.05);
        box-shadow: 0 0 12px #7046fa;
    }
    .heart-button {
        font-size: 30px;
        color: #ff446a;
        cursor: pointer;
        user-select: none;
        transition: transform 0.3s ease;
        display: inline-block;
    }
    .heart-button:hover {
        transform: scale(1.3);
        color: #ff1a3c;
    }
    .favorites-list {
        background: rgba(45,34,55,0.8);
        border-radius: 13px;
        padding: 20px;
        margin-top: 16px;
    }
    </style>
""", unsafe_allow_html=True)

# Title and subtitle
st.markdown("<h1 style='color:#90a6ff;'>Study <span style='color:#a77fff;'>Spark✨</span></h1>", unsafe_allow_html=True)
st.markdown("Your daily dose of student motivation.", unsafe_allow_html=True)

# Display quote
quote, author = quotes[st.session_state.quote_idx]
st.markdown(f"""
    <div class='quote-box'>
        &ldquo;{quote}&rdquo;
        <div style='color:#b1b2fc; font-size:18px; margin-top:10px;'>– {author}</div>
    </div>
""", unsafe_allow_html=True)

# Heart button for adding to favorites
heart_clicked = st.button(":heart:", key="heart_button")
if heart_clicked:
    full_quote = f'"{quote}" – {author}' if author else f'"{quote}"'
    if full_quote not in st.session_state.favorites:
        st.session_state.favorites.append(full_quote)

# Navigation buttons with animation by default from CSS above
col1, col2 = st.columns(2)
with col1:
    if st.button("← Previous Spark", key="prev", help="Go to previous quote"):
        st.session_state.quote_idx = (st.session_state.quote_idx - 1) % len(quotes)
with col2:
    if st.button("Next Spark →", key="next", help="Go to next quote"):
        st.session_state.quote_idx = (st.session_state.quote_idx + 1) % len(quotes)

# Favorites section
st.markdown("<h3 style='margin-top:32px;'>Your Favorite Sparks <span style='heart'>&#10084;&#65039;</span></h3>", unsafe_allow_html=True)
if st.session_state.favorites:
    with st.container():
        for fav in st.session_state.favorites:
            st.markdown(f"<div class='favorites-list'>{fav}</div>", unsafe_allow_html=True)
else:
    st.markdown("No favorites yet.")


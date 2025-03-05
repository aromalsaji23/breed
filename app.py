import streamlit as st
import pandas as pd
import base64

def add_bg_from_local(image_file):
    return """
    <style>
    .stApp {
        background: url("https://wallpaperaccess.com/full/2142198.jpg") no-repeat center center fixed;
        background-size: cover;
        min-height: 100vh;
        position: relative;
    }
    
    /* Override Streamlit's default padding */
    .main .block-container {
        padding-top: 1rem;
        padding-bottom: 1rem;
    }
    
    /* Custom scrollbar */
    ::-webkit-scrollbar {
        width: 10px;
    }
    
    ::-webkit-scrollbar-track {
        background: rgba(255, 255, 255, 0.1);
    }
    
    ::-webkit-scrollbar-thumb {
        background: rgba(0, 0, 0, 0.2);
        border-radius: 5px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: rgba(0, 0, 0, 0.3);
    }
    </style>
    """

def local_css():
    return """
    <style>
        /* Hide Streamlit's default elements */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        
        .main {
            background: transparent;
            padding: 1rem;
            margin: 0;
            position: relative;
            z-index: 1;
            display: flex;
            flex-direction: column;
            align-items: center;
        }
        
        .title-card {
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(8px);
            border-radius: 20px;
            padding: 1.5rem;
            margin-bottom: 2rem;
            width: 90%;
            max-width: 800px;
            text-align: center;
            border: 1px solid rgba(0, 0, 0, 0.2);
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
        }
        
        .title {
            color: white;
            font-family: 'Arial', sans-serif;
            font-size: 2.5rem;
            font-weight: bold;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
            margin-bottom: 0.5rem;
        }
        
        .search-container {
            width: 50%;
            max-width: 800px;
            margin: 1rem auto;
        }
        
        .search-box {
            background: rgba(0, 0, 0, 0.15);
            backdrop-filter: blur(5px);
            padding: 2rem;
            border-radius: 25px;
            border: 2px solid rgba(0, 0, 0, 0.3);
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2);
            transition: all 0.3s ease;
        }
        
        .search-box:hover {
            transform: translateY(-5px);
            border-color: rgba(5, 5, 5, 0.5);
        }
        
        .search-label {
            color: white;
            font-size: 1.3rem;
            font-weight: 600;
            margin-bottom: 1rem;
            text-align: center;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);
        }
        
        .stTextInput input {
            background: rgba(255, 255, 255, 0.15) !important;
            border: 2px solid rgba(0, 0, 0, 0.3) !important;
            color: white !important;
            border-radius: 15px !important;
            padding: 1rem 1.5rem !important;
            font-size: 1.1rem !important;
            width: 100% !important;
        }
        
        .results-container {
            width: 90%;
            max-width: 800px;
            display: grid;
            gap: 1.5rem;
            margin-top: 2rem;
        }
        
        .result-card {
            background: rgba(255, 197, 5, 0.1);
            backdrop-filter: blur(8px);
            padding: 1.5rem;
            border-radius: 20px;
            border: 1px solid rgba(255, 255, 255, 0.2);
            box-shadow: 0 8px 32px rgba(230, 15, 15, 0.1);
            transition: all 0.3s ease;
        }
        
        .breed-name {
            color: white;
            font-size: 1.8rem;
            font-weight: bold;
            margin-bottom: 1rem;
            padding-bottom: 0.5rem;
            border-bottom: 2px solid rgba(255, 255, 255, 0.2);
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);
        }
        
        .attributes-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 1rem;
        }
        
        .attribute {
            background: rgba(255, 255, 255, 0.05);
            padding: 1rem;
            border-radius: 12px;
            color: white;
            font-size: 1rem;
            line-height: 1.4;
            border: 1px solid rgba(255, 255, 255, 0.1);
        }
        
        .error-message {
            background: rgba(255, 99, 71, 0.2);
            color: white;
            padding: 1rem;
            border-radius: 10px;
            text-align: center;
            margin: 1rem;
        }
    </style>
    """

def load_data():
    try:
        # Attempt to load the CSV file silently without messages
        return pd.read_csv('breeds.csv', on_bad_lines='skip')
    except Exception as e:
        st.markdown('''
        <div class="error-message">
            <p>Unable to load breed data. Please try again later.</p>
        </div>
        ''', unsafe_allow_html=True)
        return None

def search_breed(breed_data, search_query):
    # Filter rows that contain the breed name in the "Breed" column
    filtered_data = breed_data[breed_data['Breed'].str.contains(search_query, case=False, na=False)]
    return filtered_data

def main():
    # Apply custom styling
    st.markdown(local_css(), unsafe_allow_html=True)
    
    # Add background image
    st.markdown(add_bg_from_local('images/pets_bg.jpg'), unsafe_allow_html=True)

    # Wrap the main content
    st.markdown('<div class="main">', unsafe_allow_html=True)
    
    # Title Card
    st.markdown('''
    <div class="title-card">
        <div class="title">Breed Explorer</div>
    </div>
    ''', unsafe_allow_html=True)

    # Load the breed data
    breed_data = load_data()

    if breed_data is not None:
        #st.markdown('<div class="search-container">', unsafe_allow_html=True)
        #st.markdown('<div class="search-box">', unsafe_allow_html=True)
        st.markdown('<div class="search-label">🔍 Find Your Perfect Breed</div>', unsafe_allow_html=True)
        search_query = st.text_input("", placeholder="Enter breed name (e.g., Golden Retriever)")
        st.markdown('</div></div>', unsafe_allow_html=True)

        if search_query:
            results = search_breed(breed_data, search_query)
            if not results.empty:
                st.markdown('<div class="results-container">', unsafe_allow_html=True)
                for index, row in results.iterrows():
                    st.markdown(f'''
                    <div class="result-card">
                        <div class="breed-name">{row['Breed']}</div>
                        <div class="attributes-grid">
                            <div class="attribute"><strong>🐾 Type:</strong> {row['Animal Type']}</div>
                            <div class="attribute"><strong>⏳ Lifespan:</strong> {row['Average Lifespan (years)']} years</div>
                            <div class="attribute"><strong>📏 Size:</strong> {row['Size Category']}</div>
                            <div class="attribute"><strong>🎭 Temperament:</strong> {row['Temperament']}</div>
                            <div class="attribute"><strong>🏠 Apartment:</strong> {row['Suitable for Apartment']}</div>
                            <div class="attribute"><strong>✂️ Grooming:</strong> {row['Grooming Needs']}</div>
                            <div class="attribute"><strong>🎓 Training:</strong> {row['Trainability']}</div>
                        </div>
                    </div>
                    ''', unsafe_allow_html=True)
                st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()

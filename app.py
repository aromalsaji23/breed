import streamlit as st
import pandas as pd

def load_data():
    try:
        # Attempt to load the CSV file
        breed_data = pd.read_csv('breeds.csv', on_bad_lines='skip')
        st.write("CSV loaded successfully without issues.")
        return breed_data
    except pd.errors.ParserError as e:
        st.write("Error parsing CSV file:")
        st.write(e)  # Print error details
        st.write("Attempting to skip problematic lines...")

        # Try reading the CSV again while skipping problematic lines
        try:
            breed_data = pd.read_csv('breeds.csv', on_bad_lines='skip')
            st.write("Bad lines skipped. Data loaded with potential missing entries.")
            return breed_data
        except Exception as e:
            st.write(f"An error occurred while skipping bad lines: {e}")
            return None
    except Exception as e:
        st.write(f"An unexpected error occurred: {e}")
        return None

def search_breed(breed_data, search_query):
    # Filter rows that contain the breed name in the "Breed" column
    filtered_data = breed_data[breed_data['Breed'].str.contains(search_query, case=False, na=False)]
    return filtered_data

def main():
    st.title("Dog Breed Information")
    st.write("This app displays data related to various dog breeds.")

    # Load the breed data
    breed_data = load_data()

    # Check if data was loaded successfully
    if breed_data is not None:
        st.write("Data loaded successfully.")

        # Get search query from the user
        search_query = st.text_input("Enter breed name to search:")

        if search_query:
            # Perform search when the user types something
            results = search_breed(breed_data, search_query)
            if not results.empty:
                st.write("Search Results:")
                # Display the results in a readable format (not in table format)
                for index, row in results.iterrows():
                    st.write(f"**Breed**: {row['Breed']}")
                    st.write(f"**Animal Type**: {row['Animal Type']}")
                    st.write(f"**Average Lifespan (years)**: {row['Average Lifespan (years)']}")
                    st.write(f"**Size Category**: {row['Size Category']}")
                    st.write(f"**Temperament**: {row['Temperament']}")
                    st.write(f"**Suitable for Apartment**: {row['Suitable for Apartment']}")
                    st.write(f"**Grooming Needs**: {row['Grooming Needs']}")
                    st.write(f"**Trainability**: {row['Trainability']}")
                    st.write("-" * 50)  # Separator between results
            else:
                st.write("No matching breeds found.")
    else:
        st.write("Failed to load data.")

if __name__ == "__main__":
    main()

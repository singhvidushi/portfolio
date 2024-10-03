import pandas as pd

# Load datasets
amazon_prime_data = pd.read_csv('amazon_prime_titles.csv')
disney_plus_data = pd.read_csv('disney_plus_titles.csv')
hulu_data = pd.read_csv('hulu_titles.csv')
netflix_data = pd.read_csv('netflix_titles.csv')

# Add 'Platform' column
amazon_prime_data['Platform'] = 'Amazon Prime'
disney_plus_data['Platform'] = 'Disney+'
hulu_data['Platform'] = 'Hulu'
netflix_data['Platform'] = 'Netflix'

# Function to prefix 'show_id' with platform initial
def create_unique_id(row):
    platform_initial = {
        'Netflix': 'n',
        'Hulu': 'h',
        'Amazon Prime': 'a',
        'Disney+': 'd'
    }
    return platform_initial[row['Platform']] + row['show_id']

# Apply the function to each dataset
amazon_prime_data['show_id'] = amazon_prime_data.apply(create_unique_id, axis=1)
disney_plus_data['show_id'] = disney_plus_data.apply(create_unique_id, axis=1)
hulu_data['show_id'] = hulu_data.apply(create_unique_id, axis=1)
netflix_data['show_id'] = netflix_data.apply(create_unique_id, axis=1)

# Combine datasets
combined_data = pd.concat([amazon_prime_data, disney_plus_data, hulu_data, netflix_data], ignore_index=True)

# Update standard_genres

standard_genres = {
    'Action': ['action', 'action & adventure', 'adventure', 'action-adventure', 'superhero', 'spy/espionage',
               'disaster', 'military and war', 'tv action & adventure', 'military and war'],
    'Animation': ['animation', 'anime features', 'anime series', 'anime', 'adult animation', 'cartoons'],
    'Comedy': ['comedy', 'comedies', 'stand-up comedy', 'stand up', 'sketch comedy', 'sitcom', 'parody',
               'romantic comedy', 'tv comedies', 'late night', 'stand-up comedy & talk shows'],
    'Documentary': ['documentary', 'documentaries', 'docuseries', 'biographical', 'historical', 'science & nature tv',
                    'science & technology', 'animals & nature', 'history', 'travel', 'news', 'health & wellness',
                    'medical'],
    'Drama': ['drama', 'dramas', 'tv dramas', 'soap opera / melodrama', 'anthology', 'legal',
              'black stories', 'young adult audience', 'coming of age'],
    'Family': ['family', 'kids', "children & family movies", "kids' tv", 'teen', 'teen tv shows'],
    'Horror': ['horror', 'horror movies', 'tv horror'],
    'International': ['international', 'international movies', 'international tv shows', 'british tv shows',
                      'korean tv shows', 'spanish-language tv shows', 'latino'],
    'Music': ['music', 'music & musicals', 'musical', 'music videos and concerts', 'concert film', 'dance'],
    'Romance': ['romance', 'romantic movies', 'romantic tv shows', 'romantic comedy'],
    'Science Fiction': ['fantasy', 'tv sci-fi & fantasy','science fiction', 'sci-fi & fantasy', 'sci-fi', 'tv sci-fi & fantasy'],
    'Thriller': ['thriller', 'thrillers', 'suspense', 'mystery', 'tv thrillers', 'crime', 'crime tv shows',
                 'police/cop', 'tv mysteries', 'mystery', 'tv mysteries'],
    'Reality': ['reality', 'reality tv', 'unscripted', 'game shows', 'game show / competition', 'talk show',
                'talk show and variety', 'variety', 'lifestyle', 'lifestyle & culture', 'cooking & food', 'series'],
    'Sports': ['sports', 'sports movies', 'fitness', 'health & wellness', 'survival'],
    'Faith & Spirituality': ['faith & spirituality', 'faith and spirituality'],
    'Classic & Cult': ['classic & cult tv', 'classic movies', 'cult movies', 'classics'],
    'Arts & Culture': ['arts', 'and culture', 'entertainment', 'arthouse'],
    'Talk Show': ['talk show', 'talk show and variety', 'stand-up comedy & talk shows'],
    'Teen': ['teen', 'teen tv shows', 'young adult audience'],
    'Coming of Age': ['coming of age'],
    'Other': ['news','special interest','buddy','independent movies', 'movies', 'tv shows', 'western', 'independent movies','lgbtq', 'lgbtq movies', 'lgbtq+']
}

# Create reverse mapping with lowercase keys
genre_mapping = {}
for standard_genre, original_genres in standard_genres.items():
    for original_genre in original_genres:
        genre_mapping[original_genre.lower().strip()] = standard_genre

def standardize_genres(listed_in):
    if pd.isnull(listed_in):
        return ['Unknown']
    genres = [genre.strip() for genre in listed_in.split(',')]
    standardized_genres = []
    for genre in genres:
        genre_lower = genre.lower().strip()
        standardized_genre = genre_mapping.get(genre_lower, 'Other')
        standardized_genres.append(standardized_genre)
    return standardized_genres

# Apply the updated function to the 'listed_in' column
combined_data['Genre_List'] = combined_data['listed_in'].apply(standardize_genres)

# Explode 'Genre_List'
combined_data = combined_data.explode('Genre_List')

# Rename 'Genre_List' to 'Genre'
combined_data.rename(columns={'Genre_List': 'Genre'}, inplace=True)

# Drop rows with missing 'Genre' or 'Platform'
combined_data.dropna(subset=['Genre', 'Platform'], inplace=True)

# Save to CSV
combined_data.to_csv('streaming_data_cleaned.csv', index=False)

# Display first few rows
print(combined_data.head())

# Check for genres still classified as 'Other'
other_genres_df = combined_data[combined_data['Genre'] == 'Other']
other_genres_list = other_genres_df['listed_in'].dropna().unique()

# Extract individual genres from 'Other' again
unique_other_genres = set()
for genres in other_genres_list:
    for genre in genres.split(','):
        genre_clean = genre.strip().lower()
        unique_other_genres.add(genre_clean)

print("Remaining individual genres classified as 'Other':")
print(unique_other_genres)

# Print counts
unique_titles = combined_data['show_id'].nunique()
print(f"Total unique titles: {unique_titles}")

# Count of unique titles per platform
unique_titles_per_platform = combined_data.groupby('Platform')['show_id'].nunique()
print(unique_titles_per_platform)

# Count of unique titles per genre
unique_titles_per_genre = combined_data.groupby('Genre')['show_id'].nunique()
print("Unique titles per genre after update:")
print(unique_titles_per_genre)

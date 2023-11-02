# Collaborative Filtering

Collaborative filtering is a recommendation technique used in recommendation systems to provide personalized suggestions to users based on their past interactions and behaviors. It relies on the idea that users who have agreed on various items in the past are likely to agree again in the future.

![Collaborative Filtering](https://miro.medium.com/v2/resize:fit:1400/1*3ALliiz9hG79_2xopzgyrQ.png)


**User-Based Collaborative Filtering**: Recommends items to a user based on the preferences and behaviors of other users who are similar to them.

**Item-Based Collaborative Filtering**: Recommends items to a user based on their interactions with similar items.


![Collaborative Filtering](static/cosine_vector_similarity.png)

<details>
<summary style="font-size: 20px;">Dependencies</summary>
To install the required Python packages you can use the following command:

```bash
pip install -r requirements.txt
```
</details>

<details>
<summary style="font-size: 20px;">Datasets Reference</summary>
This dataset has been compiled by Cai-Nicolas Ziegler in 2004, and it comprises of three tables for users, books, and ratings.

Explicit ratings are expressed on a scale from 1-10 (higher values denoting higher appreciation) and implicit rating is expressed by 0.
</details>

<details>
<summary style="font-size: 20px;">Collaborative Filtering Recommendation Model</summary>

Step 1: Collect Datasets
- `Books.csv`: Information about books.
- `Users.csv`: User data with user IDs.
- `Ratings.csv`: User-book interaction data with user ratings.

Step 2: Data Preprocessing
- Handle missing values, if any.
- Ensure data consistency and accuracy.
- Remove duplicates and irrelevant columns.

Step 3:  Popularity-Based Recommendation
- Calculate popularity scores for books

Step 4: Implement Collaborative Filtering Recommendation
- Compute user similarities based on past interactions.
- Identify similar users for each target user.
- Recommend books based on similar users preferences.

Step 6: Demo Showcase
- Showcase the collaborative filtering recommendation system demo in flask application
- Continuously monitor and update the model as more data becomes available.
</details>

<details>
<summary style="font-size: 20px;">Run <i>model.ipynb</i></summary>
Generate all the binary pkl and csv files needed to run the demo showcase
</details>

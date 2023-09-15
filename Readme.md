## Content-Based Recommenders

A content-based recommender system suggests items to users based on the content or characteristics of the items and a user's preferences. It recommends items that are similar in content to those the user has previously shown interest in.

Content-based recommendation systems are chosen for several reasons, depending on the context and requirements of the application:

- Item Description: Content-based recommenders are well-suited for situations where items have rich and structured descriptions or attributes. For example, in the case of movies, you have information like genres, actors, directors, and plot summaries that can be used as features to describe the content of each movie.

- Cold Start Problem: Content-based systems can handle the "cold start" problem, where there is limited or no user interaction data available for new users. Since content-based recommenders rely on item features, they can make recommendations for users based solely on their preferences inferred from the item features.
- Diverse Recommendations: Content-based recommenders can provide recommendations that are diverse in terms of content. If a user has interacted with items from different genres, a content-based system can recommend items from those genres.
- Feature Engineering: Content-based systems allow for explicit feature engineering to capture item characteristics. You can design and select features that are likely to influence user preferences.

But still some limitation of content based recommendation are it may not capture the popularity or novelty of items, also single dependency, challenges while scaling and also it may not adapt well to evolving user interests.

Some topics where we can implement content based recommendation in more nice way are:

- Movie Recommendations
- Music Recommendations
- Book Recommendations
- Job Recommendations
- E-commerce Recommendations  
  etc

---

**Deriverables done in this repo include content based recommendor that takes a book title as input and returns a list of recommended book titles based on content similarity.**

---

## Collaborative-filtering-Based Recommenders

Collaborative filtering is a recommendation technique that makes personalized recommendations for users based on the preferences and behavior of other users. It assumes that users who have shown similar preferences in the past will continue to have similar preferences in the future. Collaborative filtering can be categorized into two main types:

- User-Based Collaborative Filtering:  
  In user-based collaborative filtering, recommendations are made by identifying users who are similar to the target user in terms of their interactions with items.
- Item-Based Collaborative Filtering:  
  In item-based collaborative filtering, recommendations are made by identifying items that are similar to the ones the target user has already interacted with.

Collaborative filtering is based on the idea of "wisdom of the crowd" and is effective at providing personalized recommendations. It doesn't require explicit knowledge of item features or descriptions. Instead, it relies on the historical behavior of users to make recommendations.

Collaborative filtering has been widely used in various recommendation systems, including movie recommendations, product recommendations in e-commerce, music recommendations, and more.

It does not rely on specific topics or genres; instead, it identifies similarities between users or items (movies, in this case) based on user ratings.

---

**Deriverables done in this repo include collaborative-filtering- based recommendor that takes a movie id as input and returns a list of recommended movies titles based on their past interactions or behaviors.**

---

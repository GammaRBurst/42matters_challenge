# Challenge 1: App categorization

## Question
You are given millions of apps and a list of thousands of app categories (names only e.g. "Soccer games", "Gardening Apps"). Your task is to assign each app to at least one of the app categories. Each app has a title, description and icon.

- How would you solve this problem?
- How would you verify its quality?
- How would you handle the case of adding or removing a category?
- How would you handle the case of adding or removing an app?

### Deliverables
- Description about the chosen approach and its pros and cons (no code required)
- Short discussion about alternative approaches you might have considered and their pros and cons

## Problem analysis
This problem can be labelled as "*unsupervised text classification*". It means that there is no association between apps and categories to learn from. While it is possible to create a sample to change this to a *supervised text classification* problem, it would require finding at least 10 apps for each category, which in turn requires reading tens or hundreds of thousands app descriptions, a task that may require weeks to be completed.

## Solution
Fortunately there exist algorithms like [**Lbl2Vec**](https://github.com/sebischair/Lbl2Vec) that can find matches between a set of categories and a set of documents (the apps' descriptions in this case), and assign the closest category to each app. The algorithm assigns only one category to each app, but it can be adapted to assign every category that sufficiently matches each app's description.

## Quality verification
A first quality verification can be achieved by sampling random apps and manually checking their categories. While this is a necessary step during the development phase, it is by no means a measure of the quality of the predictions. An interesting solution to the problem of quality verification could be letting the app users vote on the assigned categories. While this solution requires a specific infrastructure, time, and users willing to judge the results of the algorithm, it may be a way to steer this from an unsupervised problem to a supervised one.

## Adding and removing categories
Changing the list of available categories requires training the Lbl2Vec algorithm from the start. Depending on the execution time, it may be wise to limit the number of times this operation is performed.  
If the users' vote is implemented, there is also the need to include its results into the algorithm, so that the users' input does not go to waste.

## Adding and removing apps
While adding or removing categories can be an intensive task, the same is not true for apps. The Lbl2Vec algorithm can predict the category of a new app using the old training data without the need to restart the training. Removing an app is even simpler, because it requires no additional computation.


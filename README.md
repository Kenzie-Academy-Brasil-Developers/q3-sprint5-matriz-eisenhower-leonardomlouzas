# Eisenhower Matrix

This is an API made in Flask and PostgreSQL that implements Eisenhower Matrix for time management.
Using the Eisenhower Decision Principle, tasks are evaluated using the criteria important/unimportant and urgent/not urgent, and then placed in according quadrants in an Eisenhower Matrix. Tasks in the quadrants are then handled as follows:

1. Important/Urgent quadrant tasks are done immediately and personally, e.g. crises, deadlines, problems.
2. Important/Not Urgent quadrant tasks get an end date and are done personally, e.g. relationships, planning, recreation.
3. Unimportant/Urgent quadrant tasks are delegated, e.g. interruptions, meetings, activities.
4. Unimportant/Not Urgent quadrant tasks are dropped, e.g. time wasters, pleasant activities, trivia.

## Categories Routes
| Endpoint            | Methods | Rule                      |
| :------------------ | :-----: | :-----------------------: |
| create_category     | POST    | /categories               |
| retrieve_categories | GET     | /categories               |
| fix_category        | PATCH   | /categories/<category_id> |
| remove_category     | DELETE  | /categories/<category_id> |

**This project was made for the Kenzie Academy Brasil bootcamp.**

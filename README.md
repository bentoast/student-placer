# student-placer
This is a simple proof of concept to divide students into groups

A local school district will be doing "hybrid" model, where roughly half the students come in two days a week, the other half come in two other days a week.
There's an issue where we want to keep families on the same day to reduce the number of trips parents have to take.
We're assuming that families have the same last name. So while not all the Smiths are in the same family, but everyone in a certain household is a Smith.
We also don't want the situation where teachers have 20 one day and 10 the other, we'd like to keep them roughly equal.

So we implement a sort of priority bucket system.

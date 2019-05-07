/*175. Combine Two Tables */
SELECT person.FirstName,person.LastName,Address.City,Address.State from person
full outer join on
person.PersonId = Address.PersonId'
ORDER BY person.PersonId;
-- Keep a log of any SQL queries you execute as you solve the mystery.
.schema

--checking interviews--
SELECT description
FROM crime_scene_reports
WHERE month = 7 AND day = 28
AND street = 'Humphrey Street';

--finding clues in the case--
SELECT id, name, transcript
FROM interviews
WHERE month = 7 AND day = 28
AND year = 2021;

--who drove from bakery at specified time--
SELECT activity, license_plate, id, minute
FROM bakery_security_logs
WHERE month = 7 AND day = 28
AND hour = 10 AND minute > 15 AND minute <26 AND activity ='exit';

--who took cash --
SELECT id, account_number, transaction_type, amount
FROM atm_transactions
WHERE month = 7 AND day = 28
AND year = 2021 AND atm_location = 'Leggett Street' AND transaction_type = 'withdraw';


SELECT person_id
FROM bank_accounts
WHERE account_number IN (SELECT account_number FROM atm_transactions WHERE month = 7 AND day = 28 AND year = 2021 AND atm_location = 'Leggett Street' AND transaction_type = 'withdraw');

--who flew off from the city with the first flight--
SELECT id, destination_airport_id, hour
FROM flights
WHERE origin_airport_id =
(SELECT id FROM airports WHERE city = 'Fiftyville')
AND year = 2021
AND month = 7
AND day = 29
ORDER BY hour;

SELECT passport_number, seat
FROM passengers
WHERE flight_id = 36;

--who called who--
SELECT id, caller, receiver, duration
FROM phone_calls
WHERE month = 7 AND day = 28 AND year = 2021 AND duration < 60
ORDER BY duration;

--putting all the pieces together--
SELECT id, name, phone_number, passport_number, license_plate
FROM people
WHERE
phone_number IN
(SELECT caller
FROM phone_calls
WHERE month = 7 AND day = 28 AND year = 2021 AND duration < 60)

AND passport_number IN
(SELECT passport_number
FROM passengers
WHERE flight_id = 36)

AND license_plate IN
(SELECT license_plate
FROM bakery_security_logs
WHERE month = 7 AND day = 28
AND hour = 10 AND minute > 15 AND minute <26 AND activity ='exit')

AND id IN
(SELECT person_id
FROM bank_accounts
WHERE account_number IN
(SELECT account_number FROM atm_transactions
WHERE month = 7 AND day = 28 AND year = 2021 AND atm_location = 'Leggett Street'
AND transaction_type = 'withdraw'));

--finding the airport--
SELECT city
FROM airports
WHERE id = 4;

--finding the call reciever--
SELECT name
FROM people
WHERE phone_number = '(375) 555-8161';

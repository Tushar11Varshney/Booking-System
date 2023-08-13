## COVID-19 Vaccine Appointment Booking System

### Problem Statement

In the given scenario, our task is to develop a booking system for efficiently scheduling appointments for COVID-19 vaccine shots. With a fixed capacity of 120 seats, our system must cater to a maximum of 120 patients at any given time. The primary objective is to establish a reliable and effective system that streamlines the seat booking process. The pivotal challenge is to seamlessly manage potential surges in booking attempts from users, surpassing the seat capacity of 120, while avoiding confusion and conflicting reservations. To conquer this challenge, we will implement a pessimistic locking mechanism. This mechanism will ensure precise synchronization, fostering an organized booking process, even when inundated with a substantial volume of simultaneous booking requests.

### Core Requirements

1. Each seat can only be allocated to a single patient, and once assigned, seat transfers are not permitted.
2. Assumption: All 120 individuals attempting to book seats are doing so simultaneously.

### Micro Requirements

1. Guarantee the consistency of data within the system, preventing any state of inconsistency.
2. Eliminate the possibility of deadlocks (if applicable), ensuring the system's stability.
3. Ensure that the system's throughput remains unaffected by the locking mechanism. If the throughput is affected, provide a clear explanation of the impact.

### Learning Outcomes

Through this project, you will gain valuable insights into the following areas:

- **Database Locking:** Understand the concept of database locking and how it contributes to maintaining data integrity and preventing conflicts in concurrent operations.
- **Database Schema Design:** Explore the process of designing an efficient database schema that supports the booking system's requirements and optimizes performance.

By successfully completing this project, you will enhance your proficiency in designing and developing systems that can handle high volumes of concurrent transactions while maintaining data consistency and system stability.
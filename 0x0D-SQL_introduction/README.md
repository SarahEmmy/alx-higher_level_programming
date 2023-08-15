# Project 0x0D-SQL_introduction

## Hey there, Welcome to Project 0x0D-SQL_introduction!

Imagine diving into a treasure trove of data where you can explore, manipulate, and manage information just the way you want. That's what this project is all about - introducing you to the fascinating world of databases and SQL (Structured Query Language). By the time you're done, you'll have a solid understanding of how databases work, especially relational databases, and you'll be able to communicate with them using SQL. It's like unlocking a secret code to access and control data!

## What Will You Learn?

This project isn't just about codes and commands; it's about grasping some really cool concepts. Here's what you'll achieve:

### General

- You'll get the lowdown on what a database is and why it's so darn important in the world of software.
- Ever heard of a relational database? You'll become buddies with this concept and see how data gets organized.
- SQL is an acronym you'll soon know by heart. We'll explain what it stands for and why it's a game-changer.
- Say "Hello!" to MySQL, a popular database management system. You'll learn the ropes of creating databases and using fancy terms like Data Definition Language (DDL) and Data Manipulation Language (DML).
- Ever dreamt of building your own table? You'll learn how to do just that, plus how to tweak and adjust it like a pro.
- Fancy grabbing specific data from a table? You'll become a SELECT expert, picking out data like a true detective.
- Sometimes you want to be a data wizard and insert, update, or delete stuff. SQL's got you covered, and you'll master these skills.
- Subqueries might sound mysterious, but we'll demystify them and show you how to handle some really advanced queries.
- And finally, you'll learn how to use special MySQL functions to work magic with your data.

## What's Expected of You

Now, before you dive in, let's talk about a few house rules:

- You'll be doing your coding in some popular text editors like vi, vim, or emacs.
- Your code will strut its stuff on Ubuntu 20.04 LTS with MySQL 8.0 (version 8.0.25).
- Oh, and one more thing: All your SQL scripts should end with a new line. A small thing, but it makes a big difference!
- Every time you write a SQL query, give it a friend - a comment just before it to explain what it's all about.
- When you're writing your SQL scripts, start each file with a comment explaining which task it's tackling.
- To keep things tidy, write your SQL keywords in uppercase. We're talking words like SELECT and WHERE - shout them out loud!

## Getting Your Hands Dirty

Time to roll up your sleeves and start working on the project:

1. First, grab a copy of the project repository. You'll find it through the link we've given you.
2. Fire up your terminal and navigate to the project directory. This is where the magic happens.
3. Dive into the task descriptions. These are your mission briefs, telling you exactly what's expected.
4. Let your creativity flow as you write SQL scripts for each task. Don't forget to meet the project requirements!
5. Test your SQL scripts. Run them to make sure they give you the right answers - we're looking for accuracy here.
6. A great project needs a great README.md file. Compile a report that sums up your work and your newfound skills.

## Extra Resources

Here are a few extras to help you along the way:

- Check out SQL tutorials and documentation. They're like your GPS through the world of databases.
- Dive into online SQL simulators and practice platforms. It's like your training ground before the big game.
- Need a little help? Online communities and forums are like having a mentor at your fingertips.
- Books and online courses about databases and SQL are like your secret weapons. Dive into them if you need more insights.

But remember, we're here to help too. Don't hesitate to reach out if you're stuck or have questions.

## Submission and Integrity

Now, we've got some ground rules to cover:

- When you're ready to show off your hard work, follow the submission guidelines we've given you.
- We believe in doing your own thing. Copying and pasting someone else's work isn't cool - it won't help you or anyone else.
- We're serious about plagiarism. No copying, and definitely no publishing any of this project's content.
- If you get caught up in any form of plagiarism, it's a strict no-no and could lead to you getting removed from the program. We're all about integrity here.

## MySQL: Setting Up and Playing

Alright, let's get you set up with MySQL on your Ubuntu 20.04 LTS system:

1. First things first, update your system's package index. Just type:

   ```bash
   sudo apt update
   ```

2. Now, let's get MySQL installed:

   ```bash
   sudo apt install mysql-server
   ```

3. To check if it's all working, verify the installation and see the version:

   ```bash
   mysql --version
   ```

4. Feeling adventurous? Connect to your MySQL server:

   ```bash
   sudo mysql
   ```

5. When you're ready to step out of the MySQL world, just type:

   ```sql
   quit
   ```

## MySQL in a Container

Ever heard of "container-on-demand"? It's like a secret hideout for MySQL:

1. Request a container with Ubuntu 20.04 - your mini-lab for MySQL magic.
2. Connect to the container via SSH or through the web terminal.
3. Launch MySQL inside your container:

   ```bash
   service mysql start
   ```

4. And here's the key: The container's credentials are root/root.

5. Want to see the databases? Run this command:

   ```bash
   cat 0-list_databases.sql | mysql -uroot -p
   ```

## Show Us What You've Got!

Once you've nailed the tasks and compiled your project files, get ready to submit. Follow the submission guidelines we've laid out for you.

## Need Help?

If you ever hit a roadblock, feel lost, or just want a friendly chat, don't hesitate to reach out. You've got friends in the community, in online forums, and of course, the course instructors are here to support you.

This project is your chance to master SQL and open doors to exciting opportunities in software development. Embrace the learning journey, enjoy the process, and get ready to wow the world with your new SQL skills!

Happy coding!
Author : SARAHEMMY BAWA
Date : 16th 08 2023

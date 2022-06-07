#### Instagram Clone

Instagram is an American photo and video sharing social networking service founded in 2010 by Kevin Systrom and Mike Krieger, and later acquired by Facebook Inc.. The app allows users to upload media that can be edited with filters and organized by hashtags and geographical tagging.

## Technology used
1. Python
2. Django
3. HTML
4. CSS3
5. PostgresSQL
6. Bootstrap

## Requirements
An IDE such as VS code with Python version 3 installed,a terminal and a browser. 

## Setup and Instruction
1. Clone the repository at [here](https://github.com/emmakamau/InstagramClone.git).
2. Extract and open the folder on VS code or navigate to the folder on your terminal.
3. On the terminal, create a virtual environment `python3 -m venv virtual` and activate it `source virtual/bin/activate`. NB **virtual** is the name of the environment.
4. Pip install dependancies highlighted on the **requirements.txt** by running `pip install -r requirements.txt`
5. Create a **start.sh** file in the root directory of the folder and define the **secret key, email configuration**.
6. Run `chmod +x start.sh` and `./start.sh` respectively on the terminal.
7. View the application on your browser through `http://127.0.0.1:8000`.

## Behaviour Driven Development

BDD focuses on how the user will interact with the application.
What you will see and experience:
1. Sign in page, enter username and password. sign up if no account is available.
    Sign up requires a unique username, email,password. On registration, user receives an email.
2. Once signed in, you get to view the landing page with a navbar and displayed images by all users from the latest.
3. On the navbar:
- Click on **Add svg icon** to create new post.
- Click on **Profile svg icon** to navigate to your profile.
- Click on **Logout svg icon** to logout of the application.
4. Create post - Enter post name, add a caption and upload an image and submit.
5. Profile page - Displays signed in users profile with list of uploads bio and an option to edit their profile.
6. Edit profile - Allow user to edit their user name, profile picture,bio and web url if any.
7. On the landing page - Each card displays an image, comment display and comment section.
8. Click on the username to view the user profile, click on the image to display a modal with post info.

## Development
To fix a bug or enhance an existing module, follow these steps:
- Fork the repo
- Create a new branch (git checkout -b improve-feature)
- Make the appropriate changes in the files
- Add changes to reflect the changes made
- Commit your changes (git commit -am 'Improve feature')
- Push to the branch (git push origin improve-feature)
- Create a Pull Request

If you find a bug or would like to request a new function, reach out to me via Email: emmaculatewkamau@gmail.com or on [LinkedIn](https://www.linkedin.com/in/emmaculate-k-987353104/)

## License

[MIT](https://choosealicense.com/licenses/mit/)

Copyright (c) 2022 **Emmaculate Kamau**

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
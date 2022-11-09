# Medonations

Medonations is a web application created using Django, HTML, CSS, Javascript, and Google Maps API that allows people in Lebanon to donate and request non-prescription medicine from other fellow Lebanon people. 

# Link to live website 
https://medonations.herokuapp.com/


# Project Screenshots


<table>
  <tr>
    <td>Home Page (User not signed in)</td>
    <td>About Us Page</td>
  </tr>
  <tr>
    <td><img src="https://user-images.githubusercontent.com/64728439/200937768-be017bf8-6a28-4392-91f0-7f11b0770e61.png"></td>
    <td><img src="https://user-images.githubusercontent.com/64728439/200938208-455bcf9f-90c1-4398-8ec5-50801fbbfe92.png"></td>
  </tr>
  <tr>
    <td>Sign Up Page</td>
    <td>Home Page (User signed in)</td>
  </tr>
  <tr>
    <td><img src="https://user-images.githubusercontent.com/64728439/200938419-ae88adba-58b9-4a45-be8a-cfd05beebc6f.png"></td>
    <td><img src="https://user-images.githubusercontent.com/64728439/200938781-57d75a0b-0cea-4de2-9d52-f8ee25fa9ca0.png"></td>
  </tr>
  <tr>
    <td>New Donation / Request Form</td>
    <td>Deatailed Post Page</td>
  </tr>
  <tr>
    <td><img src="https://user-images.githubusercontent.com/64728439/200939037-71f3cc2c-286c-4de7-a805-4c80af35c12a.png"></td>
    <td><img src="https://user-images.githubusercontent.com/64728439/200940003-3a61c912-d990-4b9f-8a18-f077ff2486e4.png"></td>

  </tr>
  <tr>
    <td>My Posts Page</td>
  </tr>
  <tr>
    <td><img src="https://user-images.githubusercontent.com/64728439/200940134-414ec28a-c672-41d4-b6dd-8557ed79995f.png"></td>

  </tr>
 </table>
 
 # Installation and Setup Instructions
 
 Note: 
 Medonations is launched using Heroku and uses Cloudinary to store images and Google Maps API to show locations and so running the project locally on your computer will involve you setting up your own databases as I've hidden the secret codes I use for obvious security reasons. If you really want to test it locally you can set up a Heroku project and add the following key value pairs in the CONFIG VARS section found in your Heroku projects settings:
 
<ul>
  <li>SECRET_KEY</li>
  <li>CLOUDINARY_NAME (name of Cloudinary database)</li>
  <li>CLOUDINARY_API_KEY (Cloudinary database API key)</li>
  <li>CLOUDINARY_API_SECRET (Cloudinary database API secret)</li>
  <li>GOOGLE_KEY (Google API key)</li>
</ul>
 
# Reflection
Medonations is a project I started working on in the summer of 2021 while on summer vacation back home in Lebanon. The country was (and still is) in a bad socio-economic state and faces many social issues. At that time there was a large shortage of medicine in the country following the Beirut explosion and devaluation of the currency. At the same time people had anticipated this shortage and had panic bought large amount of medicine that they wouldn't use and would end up being thrown away. So the concept serves as a solution to both these issues. The ones who over bought would list their non perscription meds on the site and people in need would get in contact with them via phone. Also the ones who are in need can create request posts requesting specific medicines that can be seen by others and donated. 

In terms of technical skills I created the website using the Django web framework (HTML, CSS, Javascript) as well as the Google Maps API (for displaying maps and geolocation for location autocompletion). I launched the webiste using Heroku and Cloudinary as the backend database to store images. 

Being the first webiste I launch I faced many challenges along the way. Some included integrating the Google Maps API into the project, making content persistent (using a DB), creating a simple design that would look and work well on any device (phones, computers, tablets), and actually launching the webiste for people to use and benefit from. 











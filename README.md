# Medonations

Medonations is a web application created using Django, HTML, CSS, Javascript, and Google Maps API that allows people in Lebanon to donate and request non-prescription medicine from other fellow Lebanon people. 

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
 Download the project and open using Xcode. 
 You will need to set up your own FireBase project to host the apps configurations and data since the app won't compile without the GoogleService-Info.plist file that should be in the Resources folder.
 I am not pushing my GoogleService-Info.plist file as it will allow you to write data which I dont want. 
 Once you create your firebase project and have your GoogleService-Info.plist file add it into the resources folder as seen below:
 
 <img width="221" alt="image" src="https://user-images.githubusercontent.com/64728439/200913827-9084df8b-0191-4fd7-acfa-d8794e3f9892.png">
 
 And then you'll be able to compile and run the app and read and write data (events, etc.) 
 
# Reflection
This is a project I started working on over the summer of 2022 and I'm planning on updating in the near future, adding more features. The app, which was inspired by seeing my younger
brother not being able to book a soccer pitch because of a few friends cancelling, allows users to create and join sports events for a variety of 
sports ranging from soccer to surfing to martial arts. Each event a user creates is highly personalized to their needs with information including the location of the event,
age required, experience level, number of players needed and more. Although as of now these specifications don't stop other users that dont meet them from 
joining the event, I plan on using this data to filter out events and make the list of active events more tailored towards the current user. So only showing 
events around them, where their age meets the specification, etc. This is all to come in future updates. 

My end goal for Athlima is to connect people with similar passions together and create new friendships and memories along the way. 

The app is designed using Swift and following the MVVM (Model, View, View-Model) design pattern which allowed me to structure my code into specific parts all of which interacted together to perform complex tasks from writing and fetching
data from FireBase to setting up maps showing where each event is taking place. Having users creating and joining events and interacting with each 
other gave rise to special privacy related considerations and design choices I had to make to ensure that the app complied with Apple's privacy 
guidelines. I see great potential for the idea which is why I'm still currently working on it and planning to launch some updates in the near future. 
Updates that allow users to create private friend groups, send message invitations to others as well as involve personal trainers and a verification + point system, improving trust between users and opening the door for potential monetization.










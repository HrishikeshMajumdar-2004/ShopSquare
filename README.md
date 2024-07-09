# ShopSquare Website

I've developed an advanced Online Marketplace Website with robust features for efficient user interactions and transactions. The platform ensures secure user authentication and data protection, fostering trust among buyers and sellers.

Key features include a sophisticated user-to-user communication system that streamlines item purchasing, from discovery to transaction completion directly on the platform. Sellers benefit from a user-friendly dashboard with tools for managing product listings, including adding, editing, and deleting items, enhancing operational efficiency.

Infrastructure-wise, the website utilizes AWS S3 buckets for scalable storage of static assets and media files, ensuring optimal performance and accessibility as the platform grows.

Overall, this Online Marketplace Website offers a seamless browsing, purchasing, and selling experience, setting a high standard with its advanced functionalities.
![Screenshot 2024-07-09 085539](https://github.com/HrishikeshMajumdar-2004/ShopSquare/assets/115341865/89d3733e-e31d-4aa7-812b-399d0b1c006f)

![Screenshot 2024-07-09 085549](https://github.com/HrishikeshMajumdar-2004/ShopSquare/assets/115341865/e23b9fe9-a22a-43b9-83bf-aa4cf6b710ba)

**Item Page**

When clicking on an item, users are presented with comprehensive information such as price, seller details, images (stored in the database using Pillow), and a description. Users have the capability to edit or delete the item if they are the creator. Additionally, they can contact the seller directly should they wish to purchase the item.

The platform also displays related items from the same category as the current item, enhancing the browsing experience by suggesting similar products.

![Screenshot 2024-07-09 091558](https://github.com/HrishikeshMajumdar-2004/ShopSquare/assets/115341865/b5125667-c3aa-4475-9c47-a33a2b7d1c3d)

![Screenshot 2024-07-09 091615](https://github.com/HrishikeshMajumdar-2004/ShopSquare/assets/115341865/358c7664-2905-4fe1-9d6f-46566570aa6d)

**SignUp and Login Page**

After setting up forms for user registration by importing UserCreationForm and AuthenticationForm from django.contrib.auth, we manage the user verification process.

UserCreationForm: This form allows users to create a new account. It includes fields such as username, email, password, and password confirmation.

AuthenticationForm: This form is used for user login, with fields for username and password.

If a user attempts to log in but does not have an account, they need to sign up first. Once signed in, users gain access to additional features such as a dashboard and inbox. They can also add new items to the marketplace.

Users can sign out when they are done using the platform.

https://github.com/HrishikeshMajumdar-2004/ShopSquare/assets/115341865/fea36091-f24f-44e8-b564-d9b174b7a45a




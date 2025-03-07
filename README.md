# ShopSquare Website

I've developed an advanced Online Marketplace Website with robust features for efficient user interactions and transactions. The platform ensures secure user authentication and data protection, fostering trust among buyers and sellers.

Key features include a sophisticated user-to-user communication system that streamlines item purchasing, from discovery to transaction completion directly on the platform. Sellers benefit from a user-friendly dashboard with tools for managing product listings, including adding, editing, and deleting items, enhancing operational efficiency.

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

**Adding new Items**

The Django setup enables authenticated users to create new items through a protected view function. It utilizes a specialized form, NewItemForm, designed with fields such as category, name, description, price, and image, each styled uniformly for presentation. Upon form submission, the function validates the input, assigns the current user as the creator of the item, and redirects to the item's detail view upon successful creation. For initial page loads, the function prepares an empty form instance for users to fill out and submit. Overall, the structure ensures secure item creation within the application while enforcing user authentication.

Below is a demonstration of the logged-in user "User1" adding a new item to the website, which already contains some existing items :

https://github.com/HrishikeshMajumdar-2004/ShopSquare/assets/115341865/925135d3-c85b-43c3-b0a5-27b2e96badc0

**Dashboard**

A signed-in user can see all the items that they have created.

Below is a demonstration of the signed-up user "Rishi" being able to see all the products he has created on the website among all the other items present:

https://github.com/HrishikeshMajumdar-2004/ShopSquare/assets/115341865/3b8ed5da-6056-40cf-88a5-d85d65564b9a

**Editing and Deleting an item**

This website allows authenticated users to edit and delete details of items they own. It verifies user identity before retrieving and updating item information. When users submit changes through a form, such as editing details or deleting items, the website validates and processes the request accordingly. After editing or deleting an item, users are redirected to relevant pages for confirmation or further action. The form facilitates editing by providing fields for item name, description, price, and optional image upload, ensuring a streamlined and secure user experience for managing item information on the website.

Below is a demonstration of how a logged-in user "User1" edits and deletes an item that they created on the website:

https://github.com/HrishikeshMajumdar-2004/ShopSquare/assets/115341865/96675501-593f-4066-8a3d-3c993f9b01c8

**Browsing items**

Users can search for available items in the market using two methods: they can enter keywords into the search box to retrieve items that are not marked as sold, and they can filter items by categories. If a category ID is specified, the system filters items accordingly. Moreover, if users provide a search query, the system filters items by name or description containing the query. Additionally, users have the option to clear any applied filters. This functionality enhances the browsing experience by providing versatile ways to find specific items or explore different categories on the platform.

https://github.com/HrishikeshMajumdar-2004/ShopSquare/assets/115341865/d4ecd5b9-d667-4654-8b2a-a496d10ed191

**Conversations**

Logged-in users can engage in conversations with each other, particularly when showing interest in purchasing an item. Interested customers can contact sellers to express their interest in buying specific items. Users can check their inbox to see if they have any new messages. The website features an interactive user interface for facilitating conversations between buyers and sellers.

Below is a demonstration of logged-in user "User1" sending a message to the seller of a product, "Rishi," who has received the message:

https://github.com/HrishikeshMajumdar-2004/ShopSquare/assets/115341865/a35f9f60-9eeb-4e4c-b5f5-eebce084bae3




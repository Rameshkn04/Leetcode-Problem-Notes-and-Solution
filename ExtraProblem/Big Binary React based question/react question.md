E-commerce companies like Amazon often have a feature where they show the most popular products on their homepage. Suppose you are tasked with building a React component that displays the top 5 most popular products on the homepage of an e-commerce website. The component should fetch the data from a backend API and update itself whenever the user navigates to the homepage. The backend API returns an array of objects, each containing the product name, price, and popularity score.

Here's a sample response from the API:

[
  {
    "productName": "Product A",
    "price": 10.99,
    "popularityScore": 100
  },
  {
    "productName": "Product B",
    "price": 9.99,
    "popularityScore": 80
  },
  ...
]
Implement a React component that displays the top 5 most popular products in a list, along with their prices and popularity scores. The component should also handle errors if the API request fails.

Note: You can assume that you have access to a fetchData function that makes an HTTP request to the backend API and returns a promise that resolves with the JSON data.

import React, { useState, useEffect } from 'react';

function PopularProducts() {
 // your code here
}

export default PopularProducts;

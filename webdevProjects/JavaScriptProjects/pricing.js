// Sample product data
const products = [
    { id: 1, name: "Product 1", price: 20, imageUrl: "https://m.media-amazon.com/images/I/71pDAcQSYlL._AC_UF1000,1000_QL80_.jpg" },
    { id: 2, name: "Product 2", price: 30, imageUrl: "https://m.media-amazon.com/images/I/51fC4b3UbGL.jpg" },
    // Add more products as needed
];

// Array to store items in the cart
let cartItems = [];

// Function to display products on the page
function displayProducts() {
    const productsContainer = document.getElementById('productsContainer');
    productsContainer.innerHTML = '';
    products.forEach(product => {
        const productElement = `
            <div class="product">
                <img src="${product.imageUrl}" alt="${product.name}">
                <h3>${product.name}</h3>
                <p>$${product.price}</p>
                <button onclick="addToCart(${product.id})">Add to Cart</button>
            </div>
        `;
        productsContainer.innerHTML += productElement;
    });
}

// Function to add product to cart
function addToCart(productId) {
    const product = products.find(p => p.id === productId);
    if (product) {
        cartItems.push(product); // Add product to the cart array
        updateCart();
    }
}

// Function to remove item from cart
function removeFromCart(index) {
    cartItems.splice(index, 1); // Remove item from cart array
    updateCart();
}

// Function to update cart count and display cart items
function updateCart() {
    const cartItemsElement = document.getElementById('cartItems');
    cartItemsElement.innerHTML = ''; // Clear previous cart items

    // Add each item in the cart to the cart display
    cartItems.forEach((item, index) => {
        const cartItemElement = document.createElement('li');
        cartItemElement.innerHTML = `${item.name} - $${item.price} <button onclick="removeFromCart(${index})">Remove</button>`;
        cartItemsElement.appendChild(cartItemElement);
    });

    updateCartCount();
}

// Function to handle checkout
function checkout() {
    alert('Checkout functionality will be implemented in the backend.');
}

// Display products when the page loads
window.onload = function() {
    displayProducts();
};


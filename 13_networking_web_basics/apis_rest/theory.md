# APIs and REST: The Language of the Web

In the last lesson, we learned how to make HTTP requests. In this lesson, we will learn about **APIs** (Application Programming Interfaces) and **REST** (Representational State Transfer)—the architecture that powers almost every modern website and mobile app.

---

## 1. What is an API?
An API is a set of rules that allows one piece of software to talk to another. 
- **The Restaurant Analogy**: You (the Client) look at the Menu (the Documentation). You tell the Waiter (the API) what you want. The Waiter tells the Kitchen (the Server) and brings you back your food (the Data).

---

## 2. What is REST?
REST is a style of building APIs. A "RESTful" API follows these rules:
- **Stateless**: The server doesn't remember you between requests. Every request must contain everything the server needs to know.
- **Resources**: Everything (users, posts, products) has its own unique URL (an **Endpoint**).
- **HTTP Methods**: It uses standard methods like `GET`, `POST`, `PUT`, and `DELETE`.

---

## 3. Path vs. Query Parameters

### Path Parameters
Used to identify a **specific resource**.
- Example: `https://api.site.com/users/42` (Fetches user #42).

### Query Parameters
Used to **filter or sort** a list of resources. They start with a `?`.
- Example: `https://api.site.com/posts?userId=1&sort=desc` (Fetches posts by user #1, sorted by newest).

---

## 4. Authentication: The Key to the Door
Most professional APIs aren't completely public. You need an **API Key** or a **Bearer Token** to prove who you are.
- These are usually sent in the **Headers** of your request.
```python
headers = {"Authorization": "Bearer YOUR_SECRET_TOKEN"}
response = requests.get(url, headers=headers)
```

---

## 5. Rate Limiting
Servers have limits. If you make 1,000 requests in 1 second, the server will block you and return a **429 Too Many Requests** error. Always check the API documentation for its limits!

---

## 6. Best Practices
1. **Read the Docs**: Every API is different. Use tools like **Swagger** or **Postman** to test an API before writing any code.
2. **Hide your Keys**: Just like database passwords, never put API keys in your code. Use `.env` files.
3. **Handle 404s**: Sometimes a resource is deleted. Your code should handle cases where `requests.get()` returns a 404.

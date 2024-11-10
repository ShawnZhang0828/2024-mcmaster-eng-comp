### CyberSecurity Challenge
The reporistory contains a software system built based on [an existing project](https://github.com/ShawnZhang0828/group-decision-making-app) developed for SFWRENG 4HC3. This new repository aims at providing a secured approach for user registration and login to address the growing cyber security concerns.

### Additions Too The Original Project
1. Password hashing and verification for secure user authentication
2. JWT token generation for stateless user session management
3. Access control with token validation to restrict access to protected resources

### How to Run
1. Clone the repository to a local workspace.
2. Run the back-end server by running the following code in a terminal:
```
cd back-end
pip install -r requirements.txt
py main.py
```
3. Run the front-end application by running the following code in a separate terminal:
```
cd front-end
npm install
npx expo start -c
w
```

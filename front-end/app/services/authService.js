const LOGIN_URL = 'http://localhost:5000/auth/login'
const REGISTER_URL = 'http://localhost:5000/auth/register'

const authenticate = async (username, password) => {
    try {
        const response = await fetch(LOGIN_URL, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                username: username,
                password: password
            })
        });

        const data = await response.json();

        if (response.ok) {
            return data;
        } else {
            console.log("log in failed");
            return null;
        }

    } catch (error) {
        console.error('Error: ', error);
    }
};

const register = async (username, password, nickname) => {
    try {
        const response = await fetch(REGISTER_URL, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                username: username,
                password: password,
                nickname: nickname
            })
        });

        const data = await response.json();

        if (response.ok) {
            return data;
        } else {
            console.log("log in failed");
            return null;
        }

    } catch (error) {
        console.error('Error: ', error.message);
    }
}

export default { authenticate, register };
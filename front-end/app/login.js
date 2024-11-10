import React, { useState } from "react";
import {
    View,
    Text,
    TextInput,
    Button,
    Alert,
    KeyboardAvoidingView,
    ScrollView,
    Platform,
} from "react-native";
import { useRouter } from "expo-router";
import { useFonts } from "expo-font";

import authService from "./services/authService";
import { useUser } from "./contexts/userContext";

const LoginScreen = () => {
    const [fontsLoaded] = useFonts({
        CustomFont: require("../assets/font/PlaywriteDEGrund-Regular.ttf"),
    });

    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const router = useRouter();
    const { login } = useUser();

    const loginClicked = async () => {
        const response = await authService.authenticate(username, password);
        if (response && response !== null) {
            login(response.nickname);
            router.replace({
                pathname: "/home",
                params: { name },
            });
        } else {
            // works for Android and IOS, commented out for browser preview
            // Alert.alert("Login failed", "Invalid username");
            window.confirm(["Login failed", "Invalid username"].filter(Boolean).join('\n'))
        }
    };

    const registerClicked = async () => {
        router.push('/register');
    }

    return (
        <KeyboardAvoidingView
            behavior={Platform.OS === "ios" ? "padding" : "height"}
            style={{ flex: 1 }}
        >
            <ScrollView contentContainerStyle={{ flexGrow: 1 }}>
                <View className="flex-1 justify-center items-center bg-blue-100 p-4">
                    <Text
                        style={{ fontFamily: "CustomFont", paddingTop: 8, marginBottom: 20 }}
                        className="text-4xl font-bold mb-6"
                    >
                        EasyDecision
                    </Text>
                    <TextInput
                        placeholder="Enter username"
                        value={username}
                        onChangeText={setUsername}
                        className="border border-gray-400 rounded-lg p-3 w-3/4 mb-4 bg-white"
                    />
                    <TextInput
                        placeholder="Enter password"
                        value={password}
                        onChangeText={setPassword}
                        className="border border-gray-400 rounded-lg p-3 w-3/4 mb-4 bg-white"
                    />
                    <Button title="Login" onPress={loginClicked} />
                    <Button title="Register" onPress={registerClicked} />
                </View>
            </ScrollView>
        </KeyboardAvoidingView>
    );
};

export default LoginScreen;

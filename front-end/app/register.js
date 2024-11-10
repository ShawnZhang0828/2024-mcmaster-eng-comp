import React, { useState } from "react";
import {
    View,
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

const RegisterScreen = () => {
    const [fontsLoaded] = useFonts({
        CustomFont: require("../assets/font/PlaywriteDEGrund-Regular.ttf"),
    });

    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const [nickname, setNickname] = useState("");

    const router = useRouter();

    const registerClicked = async () => {
        const response = await authService.register(username, password, nickname);
        if (response) {
            router.replace({
                pathname: "/login",
            });
        } else {
            Alert.alert("Register failed", "Invalid Information Provided");
        }
    }

    return (
        <KeyboardAvoidingView
            behavior={Platform.OS === "ios" ? "padding" : "height"}
            style={{ flex: 1 }}
        >
            <ScrollView contentContainerStyle={{ flexGrow: 1 }}>
                <View className="flex-1 justify-center items-center bg-blue-100 p-4 pb-[50%]">
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
                    <TextInput
                        placeholder="Enter nickname"
                        value={nickname}
                        onChangeText={setNickname}
                        className="border border-gray-400 rounded-lg p-3 w-3/4 mb-4 bg-white"
                    />
                    <Button title="Register" onPress={registerClicked} />
                </View>
            </ScrollView>
        </KeyboardAvoidingView>
    );
};

export default RegisterScreen;

//Modules
import gptAvatar from "@/assets/logo2.png";
import warning from "@/assets/warning.svg";
import user from "@/assets/user.png";
import { useRef } from "react";
import { useChat } from "@/store/chat";
import { useForm } from "react-hook-form";
import { useAutoAnimate } from "@formkit/auto-animate/react"
import { useMutation } from "react-query";

//Components
import { Input } from "@/components/Input";
import { FiSend } from "react-icons/fi";
import {
    Avatar,
    IconButton,
    Spinner,
    Stack,
    Text
} from "@chakra-ui/react";
import ReactMarkdown from 'react-markdown'
import { Instructions } from "../Layout/Instructions";

export interface ChatProps { };

interface ChatSchema {
    input: string
};

export const Chat = ({ ...props }: ChatProps) => {
    const {
        selectedChat,
        addMessage,
        addChat,
        editChat,
        chat
    } = useChat();
    const selectedId = selectedChat?.id,
        selectedRole = selectedChat?.role;

    const hasSelectedChat = selectedChat && selectedChat?.content.length > 0;

    const {
        register,
        setValue,
        handleSubmit
    } = useForm<ChatSchema>();

    const overflowRef = useRef<HTMLDivElement>(null);
    const updateScroll = () => {
        overflowRef.current?.scrollTo(0, overflowRef.current.scrollHeight);
    };
    const [parentRef] = useAutoAnimate();
    const { mutate, isLoading } = useMutation({
    mutationKey: 'prompt',
    mutationFn: async (prompt: string) => {
        const response = await fetch(
            `http://127.0.0.1:8000/chat?query=${prompt}`
        );

        return response;
    }
    });

    const handleAsk = async ({ input: prompt }: ChatSchema) => {
        updateScroll();
        const sendRequest = (selectedId: string) => {
            setValue("input", "");

            addMessage(selectedId, {
                emitter: "user",
                message: prompt
            });

            mutate(prompt, {
                onSuccess: async (response, variable) => {
                    if (!response.body) return;

                    const reader = response.body.getReader();
                    const decoder = new TextDecoder();

                    let fullText = "";

                    // 👇 Add empty GPT message first
                    addMessage(selectedId, {
                        emitter: "gpt",
                        message: ""
                    });

                    while (true) {
                        const { done, value } = await reader.read();
                        if (done) break;

                        const chunk = decoder.decode(value);
                        fullText += chunk;

                        while (true) {
                            const { done, value } = await reader.read();
                            if (done) break;

                            const chunk = decoder.decode(value);
                            fullText += chunk;

                            // 👇 get latest chat from store
                            const latestChat = chat.find(c => c.id === selectedId);
                            if (!latestChat) break;

                            // 👇 update last message without overwriting previous messages
                            editChat(selectedId, {
                                content: latestChat.content.map((msg, i, arr) => {
                                    if (i === arr.length - 1) {
                                        return { ...msg, message: fullText };
                                    }
                                    return msg;
                                })
                            });

                            updateScroll();
                        }

                        updateScroll();
                    }
                },
                onError(error) {
                    type Error = {
                        response: {
                            data: {
                                error: {
                                    code: "invalid_api_key" | string,
                                    message: string
                                };
                            },
                        },
                    };

                    const { response } = error as Error,
                        message = response.data.error.message;
                    addMessage(selectedId, {
                        emitter: "error",
                        message
                    });
                    updateScroll();
                }
            });
        };

        if (selectedId) {
            if (prompt && !isLoading) {
                sendRequest(selectedId);
            };
        } else {
            addChat(sendRequest);
        };
    };

    return (
        <Stack
            width="full"
            height="full"
        >
            <Stack
                maxWidth="768px"
                width="full"
                marginX="auto"
                height="85%"
                overflow="auto"
                ref={overflowRef}
            >
                <Stack
                    spacing={2}
                    padding={2}
                    ref={parentRef}
                    height="full"
                >
                    {(hasSelectedChat) ? (
                        selectedChat?.content?.map(({ emitter, message }, key) => {
                            const getAvatar = () => {
                                switch (emitter) {
                                    case "gpt":
                                        return gptAvatar;
                                    case "error":
                                        return warning;
                                    default:
                                        return user;
                                }
                            };

                            const getMessage = () => {
                                if (message.slice(0, 2) == "\n\n") {
                                    return message.slice(2, Infinity);
                                };

                                return message;
                            };

                            return (
                                <Stack
                                    key={key}
                                    direction="row"
                                    padding={4}
                                    rounded={8}
                                    backgroundColor={
                                        (emitter == 'gpt') ? ("blackAlpha.200") : ("transparent")
                                    }
                                    spacing={4}
                                >
                                    <Avatar
                                        name={emitter}
                                        src={getAvatar()}
                                    />
                                    <Text
                                        whiteSpace="pre-wrap"
                                        marginTop=".75em !important"
                                        overflow="hidden"
                                    >
                                        <ReactMarkdown >
                                            {getMessage()}
                                        </ReactMarkdown>
                                    </Text>
                                </Stack>
                            )
                        })
                    ) : (
                        <Instructions
                            onClick={(text) => setValue('input', text)}
                        />
                    )}
                </Stack>
            </Stack>
            <Stack
                height="20%"
                padding={4}
                backgroundColor="blackAlpha.400"
                justifyContent="center"
                alignItems="center"
                overflow="hidden"
            >
                <Stack
                    maxWidth="768px"
                >
                    <Input
                        autoFocus={true}
                        variant="filled"
                        inputRightAddon={(
                            <IconButton
                                aria-label="send_button"
                                icon={(!isLoading) ? (<FiSend />) : (<Spinner />)}
                                backgroundColor="transparent"
                                onClick={handleSubmit(handleAsk)}
                            />
                        )}
                        {...register('input')}
                        onSubmit={console.log}
                        onKeyDown={(e) => {
                            if (e.key == "Enter") {
                                handleAsk({ input: e.currentTarget.value })
                            };
                        }}
                    />
                    <Text
                        textAlign="center"
                        fontSize="sm"
                        opacity={.5}
                    >A Q&A AI assistant, that can help you know everythinkg about Qdrant. Your feedback will help us improve.</Text>
                </Stack>
            </Stack>
        </Stack>
    );
};
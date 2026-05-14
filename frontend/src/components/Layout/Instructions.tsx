import { HStack ,Stack, Heading, Icon, Button, Text, SimpleGrid } from "@chakra-ui/react";
import { IconType } from "react-icons";
import { FiBookOpen } from "react-icons/fi";

export interface IInstructionsProps {
    onClick: (text: string) => void
};

export const Instructions = ({ onClick }: IInstructionsProps) => {
    const examples = [
    "How to batch update points using Python?",
    "How does Qdrant store vectors?",
    "Explain hybrid search in Qdrant",
    "How to use filters in Qdrant queries?",
    "What is HNSW indexing?",
    "How to insert data into Qdrant?",
    "How does reranking work with ColBERT?",
    "Difference between dense and sparse vectors?",
    "How to scale Qdrant in production?"
    ];

    return (
        <Stack
            justifyContent="center"
            alignItems="center"
            height="full"
            overflow="auto">
            <Heading size="lg" marginY={8} color= "#dc244c">
                QdrantDocs
            </Heading>
            <HStack spacing={2} align="center" bg="blackAlpha.200" px={3} py={2} borderRadius="md">
                <Icon as={FiBookOpen} color= "#dc5774" boxSize={5} />
                <Heading size="sm" color="#dc5774">Try asking</Heading>
            </HStack>
            <SimpleGrid
                columns={[1, 2, 3]} // responsive: 1 col mobile, 2 tablet, 3 desktop
                spacing={6}
                maxWidth="900px">
                {examples.map((text, key) => (
                    <Button
                        key={key}
                        height="fit-content"
                        padding={4}
                        onClick={() => onClick(text)}>
                        <Text whiteSpace="normal">
                            {text}
                        </Text>
                    </Button>
                ))}
            </SimpleGrid>
        </Stack>
    );
};
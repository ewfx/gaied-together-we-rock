// React Frontend Code
import React, { useState } from "react";
import axios from "axios";
import Card from "./components/ui/Card";
import CardContent from "./components/ui/CardContent";
import Button from "./components/ui/Button";  // ✅ Ensure this path is correct
import Input from "./components/ui/Input";
import Textarea from "./components/ui/Textarea";

export default function EmailProcessor() {
    const [emailBody, setEmailBody] = useState("");
    const [attachments, setAttachments] = useState([]);
    const [response, setResponse] = useState(null);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);
    
    const allowedFileTypes = ["image/jpeg", "image/png", "application/pdf"];
    const maxFileSize = 5 * 1024 * 1024; // 5MB
    
    const handleFileUpload = (event) => {
        const files = Array.from(event.target.files);
        const validFiles = files.filter(file => allowedFileTypes.includes(file.type) && file.size <= maxFileSize);
        
        if (validFiles.length !== files.length) {
            setError("Some files were ignored due to invalid type or size.");
        }
        
        setAttachments(validFiles);
    };

    const handleSubmit = async () => {
        setLoading(true);
        setError(null);
        try {
            const formData = new FormData();
            formData.append("email_body", emailBody);
            attachments.forEach((file) => formData.append("attachments", file));

            const { data } = await axios.post("/process-email", formData, {
                headers: { "Content-Type": "multipart/form-data" },
            });
            setResponse(data);
        } catch (err) {
            setError("Error processing the email. Please try again.");
        }
        setLoading(false);
    };

    return (
        <Card className="p-4 w-full max-w-2xl mx-auto">
            <CardContent>
                <h2 className="text-xl font-semibold mb-4">Email Processor</h2>
                <Textarea
                    value={emailBody}
                    onChange={(e) => setEmailBody(e.target.value)}
                    placeholder="Paste your email content here..."
                    className="mb-3"
                />
                <Input type="file" multiple onChange={handleFileUpload} className="mb-3" />
                {attachments.length > 0 && (
                    <ul className="mb-3">
                        {attachments.map((file, index) => (
                            <li key={index} className="text-sm">{file.name}</li>
                        ))}
                    </ul>
                )}
                <Button onClick={handleSubmit} disabled={loading}>
                    {loading ? "Processing..." : "Submit"}
                </Button>
                {error && <p className="text-red-500 mt-2">{error}</p>}
                {response && (
                    <div className="mt-4 p-3 border rounded">
                        <h3 className="text-lg font-semibold">Results:</h3>
                        <pre className="whitespace-pre-wrap text-sm">{JSON.stringify(response, null, 2)}</pre>
                    </div>
                )}
            </CardContent>
        </Card>
    );
}

import React from "react";

const Textarea = ({ value, onChange, placeholder, className }) => {
    return (
        <textarea
            value={value}
            onChange={onChange}
            placeholder={placeholder}
            className={`border p-2 rounded w-full ${className}`}
        />
    );
};

export default Textarea;

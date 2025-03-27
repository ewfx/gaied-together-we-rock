import React from "react";

const Input = ({ type, onChange, className }) => {
    return <input type={type} onChange={onChange} className={`border p-2 rounded ${className}`} />;
};

export default Input;

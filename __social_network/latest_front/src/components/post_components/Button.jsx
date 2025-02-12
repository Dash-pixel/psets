import React from 'react';

const Button = ({ icon, onClick, label }) => {
  return (
    <button
      onClick={onClick}
      className="flex items-center justify-center gap-2 px-4 py-2 text-white font-semibold rounded-lg shadow-md hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-400 focus:ring-opacity-75 transition ease-in-out duration-150"
    >
      <span>{label}</span>
    </button>
  );
};

export default Button;

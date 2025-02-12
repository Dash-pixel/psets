import React, { createContext, useState, useEffect } from 'react';

export const TokenContext = createContext();


export const TokenWrapper = ({children}) => {

    // here we should use state to set token with event listener
    const [token, setToken] = useState({token: localStorage.getItem('authToken'), id: localStorage.getItem('userId')});

    useEffect(() => {
        const handleStorageChange = (event) => {
            setToken({
              token: localStorage.getItem('authToken'),
              id: localStorage.getItem('userId'),
            });
        };
    
        window.addEventListener('storage', handleStorageChange);
    
        return () => {
          window.removeEventListener('storage', handleStorageChange);
        };
      }, []);
    // doesnt the fact that im using setToken in provider (down) mean then that i can call this function from inside the component though?
    return(
        <TokenContext.Provider value={{ token, setToken }}>
            {children}
        </TokenContext.Provider>
    )
};


// and inside other components usecontext token context
// should i set expration date on the tokens?
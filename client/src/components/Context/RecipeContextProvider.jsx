import React, {createContext, useEffect, useState} from 'react';

export const RecipeContext = createContext({});

const RecipeContextProvider = ({children}) => {
    const [recipes, setRecipes] = useState(null) ;
    const [ready, setReady] = useState(false) ;
    useEffect(() => {
        if(!recipes) {
            fetch(`${import.meta.env.VITE_API_URL}/recipes` ,)
                .then(res => res.json())
                .then((data) => {
                    setRecipes(data)
                    setReady(true)
                })
        }
    }, []);
    return (
        <RecipeContext.Provider value = {{recipes , setRecipes , ready , setReady}}>
            {children}
        </RecipeContext.Provider>
    );
};

export default RecipeContextProvider;
import React, {useContext, useEffect, useState} from 'react';
import {Card} from "react-bootstrap";
import './HomePage.css'
import RecipeContextProvider, {RecipeContext} from "../Context/RecipeContextProvider.jsx";
const HomePage = () => {
   // const [recipes , setRecipes] = useState([]) ;
  //    useEffect(() => {
  //     const request = async () => {
  //         const response =  await fetch(`${import.meta.env.VITE_API_URL}/recipes`)
  //         return await response.json() ;
  //     }
  //     request()
  //         .then((data) => setRecipes(data))
  //     //     fetch(`${import.meta.env.VITE_API_URL}/recipes`)
  //     //         .then((response) => response.json())
  //     //         .then((data) =>  setRecipes(data))
  //     //
  //
  // } , [])
    const {recipes , setRecipes , ready} = useContext(RecipeContext)
    if(!ready) {
        return <h1>Loading...</h1>
    }
    return (
        <>
            <h1>My recipes</h1>
            <div>
                <h3>Recipe length: {recipes.length > 0 ? recipes.length : ""}

                </h3>
            </div>
            <div className = "recipe-grid">
                {recipes && recipes.map((recipe) =>  {
                    return (
                       <Card key = {recipe.id}>
                           <Card.Body>
                               <Card.Title>{recipe.name && recipe.name}</Card.Title>
                           </Card.Body>
                           <Card.Img src = {recipe?.pictures[0]} height={300}/>
                       </Card>
                    );
                })}
            </div>
        </>
    );
};

export default HomePage;
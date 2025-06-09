import React, {useContext, useEffect, useState} from 'react';
import {Card} from "react-bootstrap";
import './HomePage.css'
import RecipeContextProvider, {RecipeContext} from "../Context/RecipeContextProvider.jsx";
import hourglass from '../../assets/hourglass.svg'
import CategoryList from "../CategoryList/CategoryList.jsx";
import DurationBadge from "../DurationBadge/DurationBadge.jsx";
import {Link} from "react-router";

const HomePage = () => {

    const [recipes, setRecipes] = useState([]);
    const [ready, setReady] = useState(false)
    useEffect(() => {
        const request = async () => {
            const response = await fetch(`${import.meta.env.VITE_API_URL}/recipes`)
            return await response.json();
        }
        request()
            .then((data) => {
                setRecipes(data)
                setReady(true)
            })

    }, [])
    // const {recipes , setRecipes , ready} = useContext(RecipeContext)
    // if(!ready) {
    //     return <h1>Loading...</h1>
    // }
    return (
        <>
            <h1>My recipes</h1>
            <div>
                <h3>Recipe count: {recipes.length > 0 ? recipes.length : ""}

                </h3>
            </div>
            <div className="recipes-container">
                {recipes && recipes.map((recipe) => {
                    return (
                        <Card key={`recipe-${recipe.id}`}>
                            <Link to={`/recipe/${recipe.id}`}>
                                <Card.Img src={recipe?.pictures[0]} height={300}/>
                                <Card.Body>
                                    <Card.Title>{recipe.name && recipe.name}</Card.Title>
                                    <CategoryList categories={recipe.categories}/>
                                    <DurationBadge duration={recipe.duration}/>
                                </Card.Body>
                            </Link>
                        </Card>
                    );
                })}
            </div>
        </>
    );
};

export default HomePage;
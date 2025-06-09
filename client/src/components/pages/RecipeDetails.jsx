import React, {use, useEffect, useState} from 'react';
import {useParams} from "react-router";
import CategoryList from "../CategoryList/CategoryList.jsx";
import DurationBadge from "../DurationBadge/DurationBadge.jsx";

const RecipeDetails = () => {
    const {id} = useParams();
    const [recipe, setRecipe] = useState(null)
    const [servings, setServings] = useState(1)
    const [ready, setReady] = useState(false)

    useEffect(() => {
        fetch(`${import.meta.env.VITE_API_URL}/recipes/${id}`)
            .then((response) => response.json())
            .then((data) => {
                setRecipe(data)
                setReady(true)
            })
    }, [id]);

     if(!recipe) {
        return <h2>Loading...</h2>
    }


    return (
        <div>
            <h1>{recipe && recipe.name}</h1>
            <CategoryList categories={recipe.categories}/>
            <DurationBadge duration={recipe.duration}/>
            <div>
                <h2>Ingredients</h2>
                <div>
                    <span>Servings:</span>
                        <input
                            type="number"
                            value={servings}
                            onChange={(event) => setServings(event.target.value)}
                        />
                </div>
                <div>
                    <ul>
                        {
                            recipe.ingredients.map((ingredient) => {
                                return(
                                    <li key={ingredient.id}>
                                        {`${servings * ingredient.quantity} ${ingredient.name}`}
                                    </li>
                                )
                            })
                        }
                    </ul>
                </div>
                <div>
                    <h2>Instructions</h2>
                    <p>{recipe && recipe.instructions}</p>
                </div>
                <h2>Pictures</h2>
                <div style={{
                    display : "flex" ,
                    flexWrap : "wrap",
                    gap: "1rem",
                    flexDirection : "row"
                }}>
                    {recipe && recipe?.pictures.map((picture) =>  {
                        return (
                            <div>
                                <img src={`${picture}`} alt=""
                                    style ={{
                                        aspectRatio : 1 ,
                                        width : 250 ,
                                        height : 200,
                                    }}
                                />
                            </div>
                        )
                    })}
                </div>
            </div>
        </div>
    );
};

export default RecipeDetails;
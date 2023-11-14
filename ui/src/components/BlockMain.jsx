import React, { useState } from "react";
import '../styles/App.css'; 
import { WaveSvg } from '../assets/icons/WaveSvg.jsx';
import { AlbumSet } from "./AlbumSet.jsx";

export const BlockMain = () => {
    const [albums, setAlbums] = useState([
        {
            id: "1",
            img: "https://bestsellingalbums.org/covers/58126.jpg",
            title: "album"
        },
        {
            id: "2",
            img: "https://bestsellingalbums.org/covers/58126.jpg",
            title: "album"
        },
        {
            id: "3",
            img: "https://bestsellingalbums.org/covers/58126.jpg",
            title: "album"
        },
        {
            id: "4",
            img: "https://bestsellingalbums.org/covers/58126.jpg",
            title: "album"
        }
    ])
    return (
        <section className="mian-block block container">
            <div className="mian-block-header">
                <h1>Что послушать.</h1>
                <WaveSvg />
            </div>
            <AlbumSet albums={ albums } />
        </section>
    )
}
import React, { useState } from "react";
import '../styles/App.css';
import { BlockMusic } from "./BlockMusic";
import music from "../assets/music.mp3";

export const AlbumItem = ({ albumInfo }) => {
    const [isPlaying, setIsPlaying] = useState(false);

    const playMusic = () => {
        setIsPlaying(true);
    }

    const pauseMusic = () => {
        setIsPlaying(false);
    }

    const [blocks, setBlocks] = useState([]);

    const handleClick = () => {
        setBlocks([...blocks, <BlockMusic albumInfo={ albumInfo } key={ blocks.length } />]);
    }

    return (
        <div className="album">
            <audio
                src={ music }
                autoPlay={ isPlaying }
            />
            <img 
                onClick={ handleClick }
                onMouseEnter={ playMusic }
                onMouseLeave={ pauseMusic }
                src={ albumInfo.img }
                alt={ albumInfo.title }
            />
            {blocks}
        </div>
    )
}
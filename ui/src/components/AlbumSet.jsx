import React from "react";
import { AlbumItem } from "./AlbumItem";
import '../styles/App.css';

export const AlbumSet = ({ albums }) => {
    return (
        <div className="album-set">
            {
                albums.map(album => {
                    return <AlbumItem albumInfo={ album } key={ album.id } />
                })
            }
        </div>
    )
}
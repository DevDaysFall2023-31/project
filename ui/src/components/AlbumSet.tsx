import React, { FC } from "react";
import { AlbumItem } from "./AlbumItem";
import '../styles/App.css';
import { GetTracksListSchema } from "../generated";

export const AlbumSet: FC<GetTracksListSchema> = ({ tracks }) => {
  return (
    <div className="album-set">
      {
        tracks.map(album => {
          return <AlbumItem albumInfo={album} key={album.id} />
        })
      }
    </div>
  )
}

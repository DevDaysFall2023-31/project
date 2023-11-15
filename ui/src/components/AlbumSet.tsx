import React, { FC } from "react";
import { AlbumItem } from "./AlbumItem";
import '../styles/App.css';
import { GetTracksListSchema, GetTrackSchema } from "../generated";

export const AlbumSet: FC<{ tracks: GetTrackSchema[], create: any }> = ({ tracks, create }) => {
  return (
    <div className="album-set">
      {
        tracks.map(album => {
          return <AlbumItem albumInfo={album} create={create} key={album.id} />
        })
      }
    </div>
  )
}

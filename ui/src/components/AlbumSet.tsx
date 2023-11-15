import React, { FC } from "react";
import { AlbumItem } from "./AlbumItem";
import '../styles/App.css';
import { GetTracksListSchema, GetTrackSchema } from "../generated";

export const AlbumSet: FC<{ tracks: GetTrackSchema[], create: any, count: number }> = ({ tracks, create, count }) => {
  return (
    <div className="album-set">
      {
        tracks.map(album => {
          return <AlbumItem albumInfo={album} create={create} count={count} key={album.id} />
        })
      }
    </div>
  )
}

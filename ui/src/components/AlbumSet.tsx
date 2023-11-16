import React, { FC, useEffect, useState } from "react";
import { AlbumItem } from "./AlbumItem";
import '../styles/App.css';
import { GetTrackSchema, GetPeakListSchema } from "../generated";
import api from "../api";
import supabase from "../supabase";

export const AlbumSet: FC<{ tracks: GetTrackSchema[], create: any, count: number, glob_index: number }> = ({ tracks, create, count, glob_index }) => {
  const [peaks, setPeaks] = useState<GetPeakListSchema>();

  // useEffect(() => {

  //   async function getPeaks() {
  //     const peak_list = await api.Backend.getPeaksPeaksPost(
  //       tracks.map((track) => track.id),
  //       {
  //         headers: {
  //           Authorization: 'Bearer ' + (await supabase.auth.getSession()).data.session.access_token
  //         }
  //       }
  //     );
  //     console.assert(tracks.length === peak_list.data.count);
  //     setPeaks(peak_list.data);
  //   }

  //   getPeaks();

  // }, [tracks]);

  return (
    <div className="album-set">
      {
        tracks.map((album, index) => {
          return <AlbumItem
            albumInfo={album}
            peak={peaks?.peaks[index]?.download_url ?? undefined}
            create={create}
            count={count}
            key={album.id}
            index={glob_index}
          />
        })
      }
    </div>
  )
}

import React from "react";
import { HeaderMenuColored } from "./component/Header";
import { VideoComponent } from "./component/VideoComponent";

function App() {
  const linkData = [
    {
      link: "https://devpost.com/software/gympose",
      label: "About",
    },
  ];


  return (
    <>
      <HeaderMenuColored links={linkData}></HeaderMenuColored>
      <VideoComponent></VideoComponent>
    </>
  );
}


export default App;

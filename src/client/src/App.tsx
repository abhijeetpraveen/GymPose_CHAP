import React from "react";
import { HeaderMenuColored } from "./component/Header";
import { VideoComponent } from "./component/VideoComponent";

function App() {
  const linkData = [
    {
      link: "https://devpost.com/submit-to/16239-mais-hacks-2022/manage/submissions/357448/project-overview",
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

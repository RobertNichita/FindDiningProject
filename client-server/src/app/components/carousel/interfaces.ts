export interface Images {
  [index: number]: {
    path: string;
    caption: string;
    link: string;
    width?: number;
    height?: number;
    //type?: 'image' | 'video'
  };
}

export interface Image {
  path: string;
  caption: string;
  link: string;
  width?: number;
  height?: number;
}

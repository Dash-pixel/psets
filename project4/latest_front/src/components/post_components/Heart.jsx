// import Empty from '../assets/Empty_heart.svg?react';
// import Full from '../assets/Full_heart.svg?react';
import {ReactSVG} from 'react-svg';

export default function Heart({ liked, onClick }) {
    return(
        <ReactSVG src={liked ? '/assets/Full_heart.svg' : '/assets/Empty_heart.svg'} onClick={onClick} />
    )
}

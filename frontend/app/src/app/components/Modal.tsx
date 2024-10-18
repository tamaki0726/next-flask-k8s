import React from "react";
import { Content } from "../types/content";

type ModalProps = {
    content: Content;
    onClose: () => void;
}

const Modal: React.FC<ModalProps> = ({ content, onClose }) => {
    return (
        <div
            style={{
                position: 'fixed',
                top: 0,
                left: 0,
                width: '100%',
                height: '100%',
                backgroundColor: 'rgba(0, 0, 0, 0.5)',
                display: 'flex',
                justifyContent: 'center',
                alignItems: 'center',
            }}
        >
            <div style={{
                backgroundColor: 'white', padding: '20px', borderRadius: '8px', minWidth: '300px', color: 'black'
            }}>
                <h2>詳細情報</h2>
                <table border={1} width="100%" cellPadding={8}>
                    <thead>
                        <tr>
                            <th>部品名</th>
                            <th>金額</th>
                            <th>数量</th>
                        </tr>
                    </thead>
                    <tbody>
                        {content.details.map((detail, index) => (
                            <tr key={index}>
                                <td>{detail.detailName}</td>
                                <td>{detail.amount}</td>
                                <td>{detail.count}</td>
                            </tr>
                        ))}
                    </tbody>
                </table>
                <button onClick={onClose} style={{ marginTop: '10px' }}>閉じる</button>
            </div>
        </div>
    );
};

export default Modal
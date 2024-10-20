'use client';

import Link from 'next/link';
import React, { useState } from 'react';
import { kongGatewayEndpoint } from '../config';

const UploadPage = () => {
    const [file, setFile] = useState<File | null>(null);
    const [message, setMessage] = useState<string>('');
    const [data, setData] = useState<string>('');

    const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        if (e.target.files && e.target.files.length > 0) {
            setFile(e.target.files[0])
        }
    };

    const handleUpload = async (e: React.FormEvent) => {
        e.preventDefault();

        if (!file) {
            setMessage('ファイルを選択してください');
            return;
        }

        const formData = new FormData();
        formData.append('file', file);

        try {
            const response = await fetch(`${kongGatewayEndpoint}/api/upload`, {
                method: 'POST',
                body: formData,
            });
            if (response.ok) {
                const res = await response.json();
                setMessage('ファイルをアップロードしました！');
                setData(res.data);
            } else {
                setMessage('アップロードに失敗しました...');
            }
        } catch (error) {
            console.error('エラー：', error);
            setMessage('エラーが発生しました');
        }
    };

    return (
        <div style={styles.container}>
            <form onSubmit={handleUpload} style={styles.form}>
                <input type="file" onChange={handleFileChange} style={styles.input} />
                <button type="submit" style={styles.button}>
                    アップロード
                </button>
            </form>
            {message && <p style={styles.message}>{message}</p>}
            {data && <p style={styles.message}>{data}</p>}
            {/* Searchへの遷移ボタン */}
            <Link href="/search">
                <button style={styles.linkButton}>検索画面へ</button>
            </Link>
        </div>
    );
}

const styles = {
    container: {
        display: 'flex',
        justifyContent: 'center',
        alignItems: 'center',
        height: '100vh',
        flexDirection: 'column' as const,
        backgroundColor: '#f5f5f5',
    },
    form: {
        display: 'flex',
        flexDirection: 'column' as const,
        alignItems: 'center',
        gap: '10px',
    },
    input: {
        padding: '10px',
    },
    button: {
        padding: '10px 20px',
        backgroundColor: '#4CAF50',
        color: 'white',
        border: 'none',
        borderRadius: '5px',
        cursor: 'pointer',
    },
    message: {
        marginTop: '20px',
    },
    linkButton: {
        padding: '10px 20px',
        cursor: 'pointer',
    },
};

export default UploadPage
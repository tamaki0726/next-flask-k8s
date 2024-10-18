"use client";

import React from 'react'
import { useEffect, useState } from 'react';
import { Content } from '../types/content';
import Modal from '../components/Modal';
import { testContents } from '../data/testContent';
import Link from 'next/link';
// import Modal from '@components/Modal';

const SearchPage = () => {
    const [data, setData] = useState<Content[]>([]);
    const [selectedContent, setSelectedContent] = useState<Content | null>(null);
    const [isModalOpen, setIsModalOpen] = useState(false);

    useEffect(() => {
        const fetchData = async () => {
            try {
                const response = await fetch('/v1/contents');
                // const result = await response.json();
                const result = testContents

                setData(result);
            } catch (error) {
                console.error('データの取得に失敗しました。', error);
            }
        };
        fetchData();
    }, [])

    const handleRowClick = (content: Content) => {
        setSelectedContent(content);
        setIsModalOpen(true);
    };

    return (
        <div>
            <h1 style={{ fontSize: "30px" }}>検索結果</h1>
            <table border={1} width="50%" cellPadding={8} style={{ borderCollapse: 'collapse', borderColor: 'black', textAlign: 'center' }}>
                <thead>
                    <tr>
                        <th style={{ border: '1px solid #ddd' }}>コンテンツ名</th>
                        <th style={{ border: '1px solid #ddd' }}>ユーザー名</th>
                        <th style={{ border: '1px solid #ddd' }}>作成日</th>
                    </tr>
                </thead>
                <tbody>
                    {data.map((content, index) => (
                        <tr key={index} onClick={() => handleRowClick(content)} style={{ cursor: 'Pointer' }}>
                            <td style={{ border: '1px solid #ddd' }}>{content.contentsName}</td>
                            <td style={{ border: '1px solid #ddd' }}>{content.userName}</td>
                            <td style={{ border: '1px solid #ddd' }}>{content.createdAt}</td>
                        </tr>
                    ))}
                </tbody>
            </table>

            {isModalOpen && selectedContent && (
                <Modal content={selectedContent} onClose={() => setIsModalOpen(false)} />
            )}

            {/* Uploadへの遷移ボタン */}
            <Link href="/upload">
                <button style={styles.linkButton}>アップロード画面へ</button>
            </Link>
        </div>
    );
}

const styles = {
    container: {
        display: 'flex',
        justifyContent: 'center',
        alignItems: 'center',
        height: '100vh', // 画面全体の中央に配置
        backgroundColor: '#f5f5f5',
    },
    table: {
        borderCollapse: 'collapse',
        width: '80%',
        maxWidth: '800px',
        textAlign: 'center', // テーブルの内容を中央寄せ
        boxShadow: '0 0 10px rgba(0, 0, 0, 0.1)',
        backgroundColor: '#ffffff',
    },
    row: {
        cursor: 'pointer',
        transition: 'background-color 0.3s',
    },
    rowHover: {
        backgroundColor: '#f0f0f0',
    },
    linkButton: {
        padding: '10px 20px',
        cursor: 'pointer',
    },
};

export default SearchPage
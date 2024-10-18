import { NextRequest, NextResponse } from 'next/server';
import fs from 'fs';
import path from 'path';

// POSTメソッドでファイルを受信する
// 実際はAPI gatewayに対してリクエストするためフロントでの動作確認用
export async function POST(request: NextRequest) {
    try {
        const data = await request.formData();
        const file = data.get('file') as File | null; // File 型にキャスト

        if (!file) {
            return NextResponse.json({ error: 'ファイルが見つかりません' }, { status: 400 });
        }

        // ファイル名を取得
        const fileName = file.name; // File 型から名前を取得
        const arrayBuffer = await file.arrayBuffer();
        const buffer = Buffer.from(arrayBuffer);

        // 保存先を指定
        const filePath = path.join(process.cwd(), 'uploads', fileName);

        // ファイルを保存
        fs.writeFileSync(filePath, buffer);

        return NextResponse.json({ message: 'ファイルアップロード成功' });
    } catch (error) {
        console.error('アップロードエラー:', error);
        return NextResponse.json({ error: 'アップロードに失敗しました' }, { status: 500 });
    }
}

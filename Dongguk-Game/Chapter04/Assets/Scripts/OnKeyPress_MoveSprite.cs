using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class OnKeyPress_MoveSprite : MonoBehaviour
{
    public float speed = 2; // �ӵ�: Inspector�� ����

    float vx = 0;
    float vy = 0;
    bool leftFlag = false;

    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        vx = 0;
        vy = 0;
        if (Input.GetKey("right"))  // ���� ������ Ű�� ������
        {
            vx = speed; // ���������� ���ư��� �̵����� �ִ´�.
            leftFlag = false;
        }
        if (Input.GetKey("left"))   // ���� ���� Ű�� ������
        {
            vx = -speed; // �������� ���ư��� �̵����� �ִ´�
            leftFlag = true;
        }
        if (Input.GetKey("up"))     // ���� �� Ű�� ������
        {
            vy = speed; // ���� ���ư��� �̵����� �ִ´�
        }
        if (Input.GetKey("down"))   // ���� �Ʒ� Ű�� ������
        {
            vy= -speed; // �Ʒ��� ���ư��� �̵����� �ִ´�
        }
    }

    private void FixedUpdate()
    {
        // �̵��Ѵ�
        this.transform.Translate(vx / 50, vy / 50, 0);
        // ���� ������ ������ �ٲ۴�
        this.GetComponent<SpriteRenderer>().flipX = leftFlag;
    }
}
